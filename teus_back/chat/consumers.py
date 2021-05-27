import json
from users.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import requests
from .serializers import ChatCreateSerializer
from .models import Chat, Room, Deal
from teus.func import send_push
import logging
logger = logging.getLogger('django')

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        logger.warning('connected')
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
        try:
            logger.warning("recieved")
            logger.warning(text_data)
            text_data_json = json.loads(text_data)
            room = text_data_json["room"]
            user = text_data_json["user"]
            message = text_data_json["message"]
            _file = text_data_json["file"]
        except Exception as e:
            logger.warning("Failed reading")
            logger.warning(text_data)
    
        logger.warning(f'receive from user -> {user}')
        payload = {
            'room': room,
            'user': user,
            'text': message
        }
        logger.warning(payload)
        chat = ChatCreateSerializer(data=payload)
        if not (message in ['', None] and message in ['', None]):  
            if chat.is_valid():
                chat.save()
                logger.warning(f'valid message from -> {user}')
            else:
                logger.warning(f'not valid message from -> {user}')
        try:
            room_obj = Room.objects.get(pk=int(room))
        except Exception:
            room_obj = None
        if room_obj:
            if room_obj.request_id.user.pk == int(user):
                room_obj.proposition_user_readed = False
                room_obj.request_user_readed = True 
                if room_obj.proposition_id.user.onesignal_token != '':
                    logger.warning('sended push proposition_id')
                    send_push(
                        'Teus message',
                        f'''TEUs {room_obj.request_id.user.first_name} отправил сообщение:\n{message}''',
                        room_obj.proposition_id.user.onesignal_token,
                        {'room':room_obj.pk}
                    )
                else:
                    logger.warning('no sended push proposition_id')
                    logger.error(f' token -> {room_obj.proposition_id.user.onesignal_token} ')
            elif room_obj.proposition_id.user.pk == int(user):
                room_obj.request_user_readed = False
                room_obj.proposition_user_readed = True
                if room_obj.request_id.user.onesignal_token != '':
                    logger.warning('sended push request_id')
                    send_push(
                        'Teus message',
                        f'''TEUs {room_obj.proposition_id.user.first_name} отправил сообщение:\n{message}''',
                        room_obj.request_id.user.onesignal_token,
                        {'room':room_obj.pk}
                    )
                else:
                    logger.warning('no sended push request_id')
                    logger.error(f'token => {room_obj.request_id.user.onesignal_token}')

            room_obj.save()
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "file": _file,
                "message": message,
                "user": user,
                "room": room,
            }
        )
# 
    # Receive message from room group
    def chat_message(self, event):
        logger.warning("recieved event")
        logger.warning(event)
        message = event['message']
        room = event['room']
        user = event['user']
        logger.warning(f'sended valid message from -> {user}')
        message_obj = None
        if event['file']: 
            if str(event['file']).isdigit():
                message_obj = int(event['file'])

                try:
                    path = f'http://api-teus.maximusapp.com{Chat.objects.get(pk=message_obj).attachment.url}'
                except Exception as e:
                    path = None
        self.send(text_data=json.dumps({
            "room": room,
            "user": user, #User.objects.get(pk=user).token,
            "message": message,
            "file": path if message_obj else None
        }))

class DealConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'handshake_%s' % self.room_name
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
        room = text_data_json['room']
        user = text_data_json['user']
        validated_owner = text_data_json['validated_owner']
        validated_customer = text_data_json['validated_customer']
        logger.warning(f'recieved  handashake from -> {user}')

        try:
            room_obj = Room.objects.get(pk=int(room))
        except Exception:
            room_obj = None
        if room_obj:
            if room_obj.request_id.user.pk == int(user) and validated_customer:
                room_obj.second_mark = True
                room_obj.save()
                if room_obj.proposition_id.user.onesignal_token not in ('', None):
                    send_push(
                        'Teus message',
                        f'''TEUs {room_obj.proposition_id.user.first_name} \nВаше предложение подтверждено. Сделка завершена''',
                        room_obj.proposition_id.user.onesignal_token,
                        {'room':room_obj.pk}
                    )
            if room_obj.proposition_id.user.pk == int(user) and validated_owner:
                room_obj.first_mark = True
                room_obj.save()
                if room_obj.request_id.user.onesignal_token not in ('', None):
                    send_push(
                        'Teus message',
                        f'''TEUs {room_obj.request_id.user.first_name} \nВаш запрос одобрили, для завершения сделки - подтвердите предложение''',
                        room_obj.request_id.user.onesignal_token,
                        {'room':room_obj.pk}
                    )
            if room_obj.second_mark and room_obj.first_mark:
                if validated_owner and validated_customer:
                    if room_obj.request_id.amount > room_obj.proposition_id.amount:
                        amount = room_obj.proposition_id.amount
                        room_obj.proposition_id.status = 'в архиве'
                        room_obj.request_id.amount -= amount
                        room_obj.proposition_id.amount = 0

                    elif room_obj.request_id.amount < room_obj.proposition_id.amount:
                        amount = room_obj.request_id.amount
                        room_obj.request_id.status = 'в архиве'
                        room_obj.proposition_id.amount -= amount
                        room_obj.request_id.amount = 0
                    else:
                        amount=room_obj.proposition_id.amount
                        room_obj.request_id.status = 'в архиве'
                        room_obj.proposition_id.status = 'в архиве'
                        room_obj.proposition_id.amount = 0
                        room_obj.request_id.amount = 0
                    Deal.objects.create(
                        room=room_obj,
                        user_request=room_obj.request_id.user,
                        user_proposition=room_obj.proposition_id.user,
                        amount=amount,
                        city=room_obj.proposition_id.city,
                        line=room_obj.proposition_id.line,
                        container=room_obj.proposition_id.container,
                    ).save()
                    room_obj.proposition_id.save()
                    room_obj.request_id.save()
                    room_obj.save()
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user': user,
                'room': room,
                'validated_owner': validated_owner,
                'validated_customer': validated_customer,
            }
        )

    # Receive message from room group'validated_owner'
    def chat_message(self, event):
        print(event)

        logger.warning(f'recieved event ->{event}')
        validated_owner = event['validated_owner']
        validated_customer = event['validated_customer']

        room = event['room']
        user = event['user']
        logger.warning(f'recieved handashake from-> {user}')
        self.send(text_data=json.dumps({
            "room": room, 
            "user": user, 
            'validated_owner': validated_owner,
            'validated_customer': validated_customer,
        }))
