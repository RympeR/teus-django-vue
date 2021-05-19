from django.db.models.fields import NullBooleanField
from rest_framework import serializers
from .models import User, Phone
from django.db.models import Q
from django.shortcuts import get_object_or_404
import logging
logger = logging.getLogger('django')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = (
            'is_admin',
            'password'
        )

    @staticmethod
    def create(validated_data):
        print(validated_data)
        logger.warning(f'created with data ->{validated_data}')
        try:
            phone = validated_data['phone'][0]
        except KeyError:
            phone = None
        except TypeError:
            phone = str(validated_data['phone'])
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
        try:
            if  isinstance(validated_data['onesignal_token'], list):
                one_signal = validated_data['onesignal_token'][0]
            else:
                one_signal = validated_data['onesignal_token']
        except KeyError:
            one_signal = None
        token = validated_data['token']
        print(f'token ->{token}')
        user = User(
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            company=company,
            image=image,
            token=token,
            onesignal_token=one_signal
        )
        user.save()
        return user
    
    @staticmethod
    def set_token(user, data):
        user.token=data['token']
        user.save()
        if not data.get('onesignal_token'):
            return None
        if isinstance(data['onesignal_token'], list):
            user.onesignal_token = data['onesignal_token'][0]
        else:
            user.onesignal_token = data['onesignal_token']
        user.save()
        return user.pk
    @staticmethod
    def update(validated_data):
        try:
            user = User.objects.filter(pk=validated_data['user_id']).first()
        except Exception as e:
            try:
                pass
            except Exception as e:
                pass
        print(user)
        print(validated_data)
        print('-'*10)
        logger.warning(f'updated with data ->{validated_data}')
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
            if  isinstance(validated_data['onesignal_token'], list):                 
                user.onesignal_token = validated_data['onesignal_token'][0]             
            else:                 
                user.onesignal_token = validated_data['onesignal_token']         
        except KeyError:             
            user.onesignal_token = None
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
