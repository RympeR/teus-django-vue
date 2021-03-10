from django.db.models.fields import NullBooleanField
from rest_framework import serializers
from .models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = (
            'is_admin',
            'password'
        )

    @staticmethod
    def create(validated_data):
        try:
            phone = validated_data['phone'][0]
        except KeyError:
            phone = None
        try:
            first_name = validated_data['first_name'][0]
        except KeyError:
            first_name = ''
        try:
            last_name = validated_data['last_name'][0]
        except KeyError:
            last_name = ''
        try:
            company = validated_data['company'][0]
        except KeyError:
            company = ''
        try:
            image = validated_data['image']
        except KeyError:
            image = None
        token = validated_data['token']
        user = User(
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            company=company,
            image=image,
            token=token
        )
        user.save()
        return user.token

    @staticmethod
    def update(validated_data):
        user = get_object_or_404(User, pk=validated_data['user_id'])
        try:
            user.phone = validated_data['phone'][0]
        except KeyError:
            user.phone = user.phone
        try:
            user.first_name = validated_data['first_name'][0]
        except KeyError:
            user.first_name = user.first_name
        try:
            user.last_name = validated_data['last_name'][0]
        except KeyError:
            user.last_name = user.last_name
        try:
            user.company = validated_data['company'][0]
        except KeyError:
            user.company = user.company
        try:
            user.image = validated_data['image'][0]
        except KeyError:
            try:
                user.image = getattr(user, 'image', None)
            except ValueError:
                user.image = None
        except ValueError:
            user.image = None
        user.save()
        return user

    @staticmethod
    def getProfile(user_id):
        user = get_object_or_404(User, pk=user_id)
        return user

    @staticmethod
    def deleteUser(user_id):
        user = get_object_or_404(User, pk=user_id)
        user = user.delete()
        return user

    @staticmethod
    def getList():
        users = User.objects.filter(is_admin=False)
        return users

    @staticmethod
    def update_password(instance, password):
        instance.password = password
        instance.save()
        return instance
