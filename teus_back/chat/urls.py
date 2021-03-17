from django.urls import path

from .views import *

urlpatterns = [
    path('rooms-request/<int:pk>', GetRoomsRequest.as_view()),
    path('rooms-proposition/<int:pk>', GetRoomsProposition.as_view()),

    path('create-room/', PostRoom.as_view()),
    path('update-room/<int:pk>', PutRoom.as_view()),
    path('delete-room/<int:pk>', GetRoom.as_view()),
    path('get-room/<int:pk>', GetRoom.as_view()),

    path('create-message/', PostChat.as_view()),
    path('update-message/<int:pk>', PutChat.as_view()),
    path('delete-message/<int:pk>', GetChat.as_view()),
    path('get-message/<int:pk>', GetChat.as_view()),
    
    path('handshake/<int:pk>', Handshake.as_view()),

    path('messages/<int:room_id>/', GetChatMessages.as_view()),
    path('', index, name='index'),
    path('<int:room_name>/', room, name='room'),
]