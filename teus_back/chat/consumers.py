import json
from users.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import requests
from .serializers import ChatCreateSerializer
from .models import Chat, Room

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print('connected')
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print('receive')
        room = text_data_json['room']
        user = text_data_json['user']
        message = text_data_json['message']
        _file = text_data_json['file']
        
        payload = {
            'room': room,
            'user': user,
            'text': message
        }
        print(payload)
        chat = ChatCreateSerializer(data=payload)
        if chat.is_valid():
            chat.save()
        else:
            print('not valid')
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'file': _file,
                'message': message,
                'user': user,
                'room': room,
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        print(event)
        message = event['message']
        room = event['room']
        user = event['user']
        
        message_obj = None
        if event['file']: 
            if str(event['file']).isdigit():
                message_obj = int(event['file'])

                try:
                    path = f'http://api-teus.maximusapp.com{Chat.objects.get(pk=message_obj).attachment.url}'
                except Exception as e:
                    path = None
        self.send(text_data=json.dumps({
            "user": user, #User.objects.get(pk=user).token,
            'message': message,
            'file': path if message_obj else None
        }))

class DealConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print('receive')
        room = text_data_json['room']
        user = text_data_json['user']
        accepted = text_data_json['accepted']
        validated_first = text_data_json['validated_first']
        validated_second = text_data_json['validated_second']

        try:
            room_obj = Room.objects.get(pk=int(room))
        except Room.DoesNotExist:
            room_obj = None
        if room_obj:
            if room_obj.request_id.pk == int(user):
                room_obj.first_mark = True
                room_obj.save()
            if room_obj.proposition_id.pk == int(user):
                room_obj.second_mark = True
                room_obj.save()
            if room_obj.second_mark and room_obj.first_mark:
                if validated_first and validated_second:
                    if room.request_id.amount > room.proposition_id.amount:
                        amount = room.proposition_id.amount
                        room.proposition_id.status = 'выполнен'
                        room.request_id.amount -= amount
                        room.proposition_id.amount = 0

                    elif room.request_id.amount < room.proposition_id.amount:
                        amount = room.request_id.amount
                        room.request_id.status = 'выполнен'
                        room.proposition_id.amount -= amount
                        room.request_id.amount = 0
                    else:
                        room.request_id.status = 'выполнен'
                        room.proposition_id.status = 'выполнен'
                        room.proposition_id.amount = 0
                        room.request_id.amount = 0

                    room.proposition_id.save()
                    room.request_id.save()
                    room.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user': user,
                'room': room,
                'accepted': accepted,
                'validated_first': validated_first,
                'validated_second': validated_second,
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        print(event)
        validated = event['validated']
        accepted = event['accepted']
        room = event['room']
        user = event['user']
        
        self.send(text_data=json.dumps({
            "room": room, 
            "user": user, 
            'accepted': accepted,
            'validated_first': validated_first,
            'validated_second': validated_second,
        }))
