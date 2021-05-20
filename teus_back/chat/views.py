from django.http import request
from users.models import User
from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer, MultiPartRenderer
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser
from datetime import datetime
from .models import Room, Chat, Deal
from .serializers import *
import requests


class PostRoom(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    queryset = Room.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = RoomCreateSerializer


class GetRoom(generics.RetrieveDestroyAPIView):
    permission_classes = (AllowAny, )
    queryset = Room.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = RoomSerializer


class PutRoom(generics.UpdateAPIView):
    permission_classes = (AllowAny, )
    queryset = Room.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = RoomCreateSerializer


class PostChat(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    queryset = Chat.objects.all()
    parser_classes = (JSONParser, MultiPartParser,
                      FileUploadParser, FormParser)
    serializer_class = ChatCreateSerializer


class GetChat(generics.RetrieveDestroyAPIView):
    permission_classes = (AllowAny, )
    queryset = Chat.objects.all()
    parser_classes = (JSONParser, MultiPartParser,
                      FileUploadParser, FormParser)
    serializer_class = ChatSerializer


class PutChat(generics.UpdateAPIView):
    permission_classes = (AllowAny, )
    queryset = Chat.objects.all()
    parser_classes = (JSONParser, MultiPartParser,
                      FileUploadParser, FormParser)
    serializer_class = ChatCreateSerializer


class GetRoomsProposition(APIView):
    permission_classes = (AllowAny, )
    queryset = Room.objects.all()
    parser_classes = (JSONParser, MultiPartParser,
                      FileUploadParser, FormParser)
    serializer_class = RoomSerializer

    def get(self, request, pk):
        try:
            user = User.objects.get(
                token=request.headers['Authorization'])
        except Exception:
            user = None

        if user:
            rooms = Room.objects.filter(
                proposition_id__user=user,
                proposition_id=pk
            )
            results = []
            domain = request.get_host()
            try:
                deals = Deal.objects.all()
                deals = [deal.room for deal in deals]
            except Exception:
                deals = []
            for obj in rooms:
                had_deal = False
                if obj in deals:
                    had_deal = True
                try:
                    path_image = obj.request_id.user.image.url
                except Exception:
                    path_image = None
                if path_image:
                    user_request_image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=path_image)
                else:
                    user_request_image_url = None
                try:
                    path_image = obj.proposition_id.user.image.url
                except Exception:
                    path_image = None
                if path_image:
                    user_proposition_image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=path_image)
                else:
                    user_proposition_image_url = None
                try:
                    path_image = obj.proposition_id.container.image.url
                except Exception:
                    path_image = None
                if path_image:
                    container_request_image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=path_image)
                else:
                    container_request_image_url = None
                results.append(
                    {
                        "id": obj.pk,
                        "line":{
                            "name": obj.proposition_id.line.name if obj.proposition_id.line.name else None,
                        },
                        "contianer":{
                            "name": obj.proposition_id.container.name,
                            "image": container_request_image_url,
                        },
                        "user_request":{
                            "id": obj.request_id.user.pk,
                            "first_name": obj.request_id.user.first_name,
                            "last_name": obj.request_id.user.last_name,
                            "image": user_request_image_url,
                        },
                        "user_proposition":{
                            "id": obj.proposition_id.user.pk,
                            "first_name": obj.proposition_id.user.first_name,
                            "last_name": obj.proposition_id.user.last_name,
                            "image": user_proposition_image_url,
                        },
                        "was_handshake": had_deal,
                        "amount": obj.request_id.amount,
                        "user_request_id": obj.request_id.pk,
                        "user_proposition_id": obj.proposition_id.pk,
                        "date": int(obj.date.timestamp()),
                        "first_mark": obj.first_mark,
                        "second_mark": obj.second_mark,
                        "readed": obj.proposition_user_readed
                    }
                )
            return Response(
                results
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )


class GetRoomsRequest(APIView):
    permission_classes = (AllowAny, )
    queryset = Room.objects.all()
    parser_classes = (JSONParser, MultiPartParser,
                      FileUploadParser, FormParser)
    serializer_class = RoomSerializer

    def get(self, request, pk):
        try:
            user = User.objects.get(
                token=request.headers['Authorization'])
        except Exception:
            user = None

        if user:
            
            rooms = Room.objects.filter(
                request_id__user=user,
                request_id=pk
            )
            results = []
            domain = request.get_host()
            try:
                deals = Deal.objects.all()
                deals = [deal.room for deal in deals]
            except Exception:
                deals = []
            for obj in rooms:
                had_deal = False
                if obj in deals:
                    had_deal = True
                try:
                    path_image = obj.request_id.user.image.url
                except Exception:
                    path_image = None
                if path_image:
                    user_request_image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=path_image)
                else:
                    user_request_image_url = None
                try:
                    path_image = obj.proposition_id.user.image.url
                except Exception:
                    path_image = None
                if path_image:
                    user_proposition_image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=path_image)
                else:
                    user_proposition_image_url = None
                try:
                    path_image = obj.request_id.container.image.url
                except Exception:
                    path_image = None
                if path_image:
                    container_request_image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=path_image)
                else:
                    container_request_image_url = None
                results.append(
                    {
                        "id": obj.pk,
                        "line":{
                            "name": obj.request_id.line.name,
                        },
                        "contianer":{
                            "name": obj.request_id.container.name,
                            "image": container_request_image_url,
                        },
                        "user_request":{
                            "id": obj.request_id.user.pk,
                            "first_name": obj.request_id.user.first_name,
                            "last_name": obj.request_id.user.last_name,
                            "image": user_request_image_url,
                        },
                        "user_proposition":{
                            "id": obj.proposition_id.user.pk,
                            "first_name": obj.proposition_id.user.first_name,
                            "last_name": obj.proposition_id.user.last_name,
                            "image": user_proposition_image_url,
                        },
                        "was_handshake": had_deal,
                        "amount": obj.proposition_id.amount,
                        "user_request_id": obj.request_id.pk,
                        "user_proposition_id": obj.proposition_id.pk,
                        "date": int(obj.date.timestamp()),
                        "first_mark": obj.first_mark,
                        "second_mark": obj.second_mark,
                        "readed": obj.request_user_readed
                    }
                )
            return Response(
                results
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )

class GetRoomInfo(APIView):
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser, MultiPartParser,
                      FileUploadParser, FormParser)
    def get(self, request, pk):
        try:
            user = User.objects.get(
                token=request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            try:
                try:
                    deals = Deal.objects.all()
                    deals = [deal.room for deal in deals]
                except Exception:
                    deals = []
                domain = request.get_host()
                room = Room.objects.get(pk=pk)
                had_deal = False
                if room in deals:
                    had_deal = True
                try:
                    path_image = room.request_id.user.image.url
                except Exception:
                    path_image = None
                if path_image:
                    user_request_image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=path_image)
                else:
                    user_request_image_url = None
                try:
                    path_image = room.proposition_id.user.image.url
                except Exception:
                    path_image = None
                if path_image:
                    user_proposition_image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=path_image)
                else:
                    user_proposition_image_url = None
                try:
                    path_image = room.request_id.container.image.url
                except Exception:
                    path_image = None
                if path_image:
                    container_request_image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=path_image)
                else:
                    container_request_image_url = None
                return Response(
                    {
                        "id": room.pk,
                        "line":{
                            "name": room.request_id.line.name,
                        },
                        "contianer":{
                            "name": room.request_id.container.name,
                            "image": container_request_image_url,
                        },
                        "user_request":{
                            "id": room.request_id.user.pk,
                            "first_name": room.request_id.user.first_name,
                            "last_name": room.request_id.user.last_name,
                            "image": user_request_image_url,
                        },
                        "user_proposition":{
                            "id": room.proposition_id.user.pk,
                            "first_name": room.proposition_id.user.first_name,
                            "last_name": room.proposition_id.user.last_name,
                            "image": user_proposition_image_url,
                        },
                        "was_handshake": had_deal,
                        "amount": room.proposition_id.amount,
                        "user_request_id": room.request_id.pk,
                        "user_proposition_id": room.proposition_id.pk,
                        "date": int(room.date.timestamp()),
                        "first_mark": room.first_mark,
                        "second_mark": room.second_mark,
                        "readed": room.request_user_readed
                    }
                )
            except Exception: 
                return Response(
                    {
                        "status": "Room with provided id does not exist"
                    }
                )

        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )
class GetChatMessages(APIView):
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser, MultiPartParser,
                      FileUploadParser, FormParser)

    def get(self, request, room_id):
        try:
            user = User.objects.get(
                token=request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            offset = int(request.GET.get('offset', 0))
            limit = int(request.GET.get('limit', 20))
            room = Room.objects.get(pk=room_id)
            objects = Chat.objects.filter(
                Q(room=room)
            ).order_by('-date')
            results = []
            domain = request.get_host()
            for obj in objects:
                try:
                    path_image = obj.attachment.url
                except Exception:
                    path_image = None
                if path_image:
                    image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=path_image)
                else:
                    image_url = None
                results.append(
                    {
                        "id": obj.pk,
                        "room_id": obj.room.pk,
                        "user_id": obj.user.pk,
                        "text": obj.text,
                        "attachment": image_url,
                        "date": int(obj.date.timestamp() * 1000 ),
                    },
                )
            return Response(
                results[offset: offset+limit]
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )


class Handshake(APIView):
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser, MultiPartParser,
                      FileUploadParser, FormParser)

    def put(self, request, pk):
        try:
            user = User.objects.get(
                token=request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            room = Room.objects.get(pk=pk)
            if request.data['handshake'] == 1:
                room.first_mark = True
            elif request.data['handshake'] == 2:
                room.second_mark = True

            if room.first_mark and room.second_mark:
                user_request = room.request_id.user.pk
                user_proposition = room.proposition_id.user.pk
                container = room.proposition_id.container.pk
                line = room.proposition_id.line.pk
                city = room.proposition_id.city.pk
                if room.request_id.amount > room.proposition_id.amount:
                    amount = room.proposition_id.amount
                    room.proposition_id.status = 'выполнен'
                    room.request_id.amount -= room.proposition_id.amount
                    room.proposition_id.amount = 0

                elif room.request_id.amount < room.proposition_id.amount:
                    amount = room.request_id.amount
                    room.request_id.status = 'выполнен'
                    room.proposition_id.amount -= room.request_id.amount
                    room.request_id.amount = 0
                else:
                    room.request_id.status = 'выполнен'
                    room.proposition_id.status = 'выполнен'
                    room.proposition_id.amount = 0
                    room.request_id.amount = 0

                room.proposition_id.save()
                room.request_id.save()
                room.save()
                domain = request.get_host()
                url = f"http://{domain}/api/containers/create-deal/"

                payload = {
                        'user_request': user_request,
                        'amount': amount,
                        'city': city,
                        'line': line,
                        'container': container,
                        'user_proposition': user_proposition
                }
                headers = {
                    'Authorization': 'tset'
                }

                response = requests.request(
                    "POST", url, headers=headers, json=payload)

                print(response.text)
                return Response(
                    {
                        "success": response.status_code,
                        "status": "processed"
                    }
                )
            else:
                return Response(
                    {
                        "status": "needs second handshake"
                    }
                )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )


def index(request):
    return render(request, 'index.html')


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })
