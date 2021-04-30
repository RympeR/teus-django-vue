from rest_framework import serializers
from .models import Room, Chat
from containers.serializers import UserPropositionsSerializer, UserRequsetSerializer
from users.serializers import UserSerializer


class TimestampField(serializers.Field):
    def to_representation(self, value):
        return value.timestamp()


class RoomSerializer(serializers.ModelSerializer):
    
    request_id = UserRequsetSerializer()
    proposition_id = UserPropositionsSerializer()
    date = TimestampField(required=False)

    class Meta:
        model = Room
        fields = '__all__'


class RoomCreateSerializer(serializers.ModelSerializer):
    date = TimestampField(required=False)

    class Meta:
        model = Room
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    date = TimestampField(required=False)
    user = UserSerializer()

    class Meta:
        model = Chat
        fields = '__all__'


class ChatCreateSerializer(serializers.ModelSerializer):
    # date = TimestampField(required=False)

    class Meta:
        model = Chat
        exclude = ('date', )

# class RoomHandshakeSerializer(serializers.ModelSerializer):
#     request_id = UserRequsetSerializer()
#     proposition_id = UserPropositionsSerializer(req)
#     date = TimestampField(required=False)

#     class Meta:
#         model = Room
#         fields = '__all__' 