from rest_framework import serializers
from .models import *
from info.serializers import ContainerSerializer, LineSerializer, CitySerializer
from users.serializers import UserSerializer


class RequestSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    city = CitySerializer()
    line = LineSerializer()
    container = ContainerSerializer()

    class Meta:
        model = UserRequest
        exclude = ('id', )

    def create(self, validated_data):
        print(validated_data)
        user_request = UserRequest.objects.update_or_create(
            user=validated_data.get('user', None),
            city=validated_data.get('city', None),
            line=validated_data.get('line', None),
            container=validated_data.get('containter', None),
            defaults={"request_date": validated_data.get('request_date'), }
        )
        return user_request

    @staticmethod
    def get_request(request_id):
        user_request=UserRequest.objects.get(pk=request_id)
        return user_request

    @staticmethod
    def delete(request_id):
        user_request = UserRequest.objects.get(pk=request_id).delete()
        return user_request[0]


class PropositionSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    city = CitySerializer()
    line = LineSerializer()
    container = ContainerSerializer()

    class Meta:
        model = UserProposition
        exclude = ('id', )

    def create(self, validated_data):
        print(validated_data)
        user_proposition = UserProposition.objects.create(
            user=validated_data.get('user', None),
            city=validated_data.get('city', None),
            line=validated_data.get('line', None),
            container=validated_data.get('container', None),
            defaults={
                "start_date": validated_data.get('start_date'),
                "end_date": validated_data.get('end_date'),
            }
        )
        return user_proposition

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.city = validated_data.get('city', instance.city)
        instance.line = validated_data.get('line', instance.line)
        instance.container = validated_data.get('container', instance.container)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.start_date)
        instance.save()
        return instance
    
    @staticmethod
    def get_propos(proposition_id):
        proposition=UserProposition.objects.get(pk=proposition_id)
        return proposition

    @staticmethod
    def delete(proposition_id):
        proposition = UserProposition.objects.get(pk=proposition_id).delete()
        return proposition[0]
