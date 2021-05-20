from rest_framework import serializers
from rest_framework import exceptions
from .models import *
from info.serializers import ContainerSerializer, LineSerializer, CitySerializer, GenericCitySerializer
from users.serializers import UserSerializer
from datetime import datetime
from rest_framework.views import APIView 
from users.models import *
from info.models import *
from chat.models import *
from rest_framework.response import Response
from rest_framework import status
class TimestampField(serializers.Field):
    def to_representation(self, value):
        return int(value.timestamp())

    def to_internal_value(self, value):
        return value


class UserRequsetSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=User.objects.all())
    container = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Container.objects.all())
    city = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=City.objects.all(), many=True)
    line = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Line.objects.all())

    class Meta:
        model = UserRequest
        fields = '__all__'

    def create(self, validated_data):
        user_request = UserRequest.objects.create(
            user=validated_data.get('user'),
            line=validated_data.pop('line', None),
            container=validated_data.pop('container', None),
            amount=validated_data.get('amount', None),
            request_date=validated_data.get('request_date', None),
            end_date=validated_data.get('end_date', None)
        )
        user_request.city.set(validated_data.pop('city'))
        user_request.save()
        return user_request


class UserPropositionsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=User.objects.all())
    container = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Container.objects.all())
    city = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=City.objects.all())
    line = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Line.objects.all())

    class Meta:
        model = UserProposition
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        user_proposition = UserProposition.objects.create(
            user=validated_data.get('user'),
            city=validated_data.pop('city', None),
            line=validated_data.pop('line', None),
            container=validated_data.pop('container', None),
            amount=validated_data.get('amount', None),
            start_date=validated_data['start_date'],
            end_date=validated_data.get('end_date', None),

        )
        return user_proposition


class RequestSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=User.objects.all())
    container = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Container.objects.all())
    city = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=City.objects.all(), many=True)
    line = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Line.objects.all())

    class Meta:
        model = UserRequest
        fields = '__all__'

    def create(self, validated_data):
        user_request = UserRequest.objects.create(
            user=validated_data.pop('user', None),
            city=validated_data.pop('city', None),
            line=validated_data.pop('line', None),
            container=validated_data.pop('container', None),
            amount=validated_data.get('amount', None),
            request_date=validated_data.get('request_date', None),
            end_date=validated_data.get('end_date', None)
        )
        return user_request

    def update(self, instance, validated_data):
        # print(validated_data)
        instance.user = validated_data.pop('user', instance.user)
        instance.city.set(validated_data.pop('city', instance.city))
        instance.line = validated_data.pop('line', instance.line)
        instance.container = validated_data.pop(
            'container', instance.container)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.request_date = validated_data.get(
            'request_date', instance.request_date)
        instance.end_date = validated_data.get(
            'end_date', instance.end_date)
        instance.status = validated_data.get(
            'status', instance.status)
        instance.save()
        return instance

    @staticmethod
    def get_request(request_id):
        user_request = UserRequest.objects.get(pk=request_id)
        return user_request

    @staticmethod
    def delete(request_id):
        user_request = UserRequest.objects.get(pk=request_id).delete()
        return user_request[0]


class DealSerializer(serializers.ModelSerializer):

    user_request = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=User.objects.all())
    user_proposition = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=User.objects.all())
    container = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Container.objects.all())
    city = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=City.objects.all())
    line = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Line.objects.all())

    class Meta:
        model = Deal
        fields = '__all__'

    def create(self, validated_data):
        deal = Deal.objects.create(
            user_request=validated_data.pop('user_request', None),
            user_proposition=validated_data.pop('user_proposition', None),
            city=validated_data.pop('city', None),
            line=validated_data.pop('line', None),
            container=validated_data.pop('container', None),
            amount=validated_data.get('amount', None),
        )
        return deal

    def update(self, instance, validated_data):
        instance.user_request = validated_data.pop(
            'user_request', instance.user_request)
        instance.user_proposition = validated_data.pop(
            'user_proposition', instance.user_proposition)
        instance.city = validated_data.pop('city', instance.city)
        instance.line = validated_data.pop('line', instance.line)
        instance.container = validated_data.pop(
            'container', instance.container)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.handshake_time = instance.handshake_time

        instance.save()
        return instance

    @staticmethod
    def get_deal(deal_id):
        deal = Deal.objects.get(pk=deal_id)
        return deal

    @staticmethod
    def delete_deal(deal_id):
        deal = Deal.objects.get(pk=deal_id).delete()
        return deal[0]


class PropositionSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=User.objects.all())
    container = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Container.objects.all())
    city = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=City.objects.all())
    line = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Line.objects.all())

    class Meta:
        model = UserProposition
        fields = '__all__'

    def create(self, validated_data):
        user_proposition = UserProposition.objects.create(
            user=validated_data.pop('user', None),
            city=validated_data.pop('city', None),
            line=validated_data.pop('line', None),
            container=validated_data.pop('container', None),
            amount=validated_data.get('amount', None),
            start_date=validated_data.get('start_date', None),
            end_date=validated_data.get('end_date', None)
        )
        return user_proposition

    def update(self, instance, validated_data):
        instance.user = validated_data.pop('user', instance.user)
        instance.city = validated_data.pop('city', instance.city)
        instance.line = validated_data.pop('line', instance.line)
        instance.container = validated_data.pop(
            'container', instance.container)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.start_date = validated_data.get(
            'start_date', instance.start_date)
        instance.end_date = validated_data.get(
            'end_date', instance.end_date)
        instance.status = validated_data.get(
            'status', instance.status)
        instance.save()
        return instance

    @staticmethod
    def get_propos(proposition_id):
        proposition = UserProposition.objects.get(pk=proposition_id)
        return proposition

    @staticmethod
    def delete(proposition_id):
        proposition = UserProposition.objects.get(pk=proposition_id).delete()
        return proposition[0]


class GetCitySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = City

class GetLineSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Line

class GetContainerSerializer(serializers.ModelSerializer):  
    image = serializers.SerializerMethodField()
    
    def get_image(self, container):
        try:
            request = self.context.get('request')
            photo_url = container.image.url
            return request.build_absolute_uri(photo_url)
        except Exception:
            return None
    class Meta:         
        fields = '__all__'         
        model = Container

class GetGenericUserSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, user):
        try:
            request = self.context.get('request')
            photo_url = user.image.url
            return request.build_absolute_uri(photo_url)
        except Exception:
            return None
    class Meta:
        fields = 'id', 'first_name', 'image'
        model = User

class GetGenericRequestSerializer(serializers.ModelSerializer):

    request_date = TimestampField(required=False)
    end_date = TimestampField(required=False)
    city = GetCitySerializer(required=False, many=True)
    container = GetContainerSerializer(required=False)
    line = GetLineSerializer(required=False)
    user = GetGenericUserSerializer(required=False)

    class Meta:
        fields = '__all__'
        model = UserRequest

class GenericRequestSerializer(serializers.ModelSerializer):
    request_date = TimestampField(required=False)
    end_date = TimestampField(required=False)
    user =  serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    def validate(self, attrs):
        print('validated')
        try:
            request = self.context.get('request')
            user = User.objects.get(
                token=request.headers['Authorization'])
            print(attrs)
            attrs['user']=user
            obj  =  None
            
            obj = UserRequest.objects.filter(
                user=attrs['user'],
                line=attrs['line'],
                city__in=attrs['city'],
                container=attrs['container'],
                request_date=attrs['request_date'],
                end_date=attrs['end_date'],
                status='в работе'
            )
            if obj:
                raise exceptions.ValidationError
            return attrs
        except Exception as e:
            print(e)
            return None
    class Meta:
        fields = '__all__'
        model = UserRequest
        
class GenericPropositionSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    
    def validate(self, attrs):
        print('validated')
        try:
            request = self.context.get('request')
            user = User.objects.get(
                token=request.headers['Authorization'])
            print(user)
            attrs['user']=user
            obj  =  None
            try:
                obj = UserProposition.objects.filter(
                    user=attrs['user'],
                    city=attrs['city'],
                    line=attrs['line'],
                    start_date=attrs['start_date'],
                    end_date=attrs['end_date'],
                    container=attrs['container'],
                    status='в работе'
                )
                print(obj, "-->obj")
            except Exception as e:
                print(e)
                pass
            
            if obj:
                raise exceptions.ValidationError
            return attrs
        except Exception as e:
            print(e)
            return None

    class Meta:
        fields = '__all__'
        model = UserProposition


class GetGenericPropositionSerializer(serializers.ModelSerializer):

    start_date = TimestampField(required=False)
    end_date = TimestampField(required=False)
    created_at = TimestampField(required=False)
    city = GetCitySerializer(required=False)
    container = GetContainerSerializer(required=False)
    line = GetLineSerializer(required=False)
    user = GetGenericUserSerializer(required=False)

    class Meta:
        fields = '__all__'
        model = UserProposition