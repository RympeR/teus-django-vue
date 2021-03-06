from rest_framework import serializers
from .models import City, Container, Line
from django.db.models import Q
from django.shortcuts import get_object_or_404



class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'

    @staticmethod
    def get(city_id):
        city = get_object_or_404(City, pk=city_id)
        return city

    @staticmethod
    def post(validated_data):
        city = City(
            name=validated_data['name']
        )
        city.save()
        return city.id

    @staticmethod
    def put(validated_data):
        city = get_object_or_404(City, pk=validated_data['city_id'])
        city.name = validated_data['name'][0]
        city.save()
        return city

    @staticmethod
    def delete(city_id):
        city = get_object_or_404(City, pk=city_id)
        try:
            city = city.delete()
        except Exception:
            pass
        return city

    @staticmethod
    def get_list():
        citites = City.objects.all()
        return citites


class ContainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Container
        fields = '__all__'

    @staticmethod
    def get(container_id):
        container = get_object_or_404(Container, pk=container_id)
        return container

    @staticmethod
    def post(validated_data):
        container = Container(
            name=validated_data['name'],
            image=validated_data['image']
        )
        container.save()
        return container.id

    @staticmethod
    def put(validated_data):
        container = get_object_or_404(
            Container, pk=validated_data['container_id'])
        container.name = validated_data['name'][0]
        try:
            container.image = validated_data['image'][0]
        except KeyError as e:
            print(e)
            container.image = container.image
        container.save()
        return container

    @staticmethod
    def delete(container_id):
        container = get_object_or_404(Container, pk=container_id)
        try:
            container = container.delete()
        except Exception as e:
            print(e)
        return container

    @staticmethod
    def get_list():
        containers = Container.objects.all()
        return containers


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Line
        fields = '__all__'

    @staticmethod
    def get(line_id):
        line = get_object_or_404(Line, pk=line_id)
        return line

    @staticmethod
    def post(validated_data):
        line = Line(
            name=validated_data['name']
        )
        line.save()
        return line.id

    @staticmethod
    def put(validated_data):
        line = get_object_or_404(Line, pk=validated_data['line_id'])
        line.name = validated_data['name'][0]
        line.save()
        return line

    @staticmethod
    def delete(line_id):
        line = get_object_or_404(Line, pk=line_id)
        try:
            line = line.delete()
        except Exception:
            pass
        return line

    @staticmethod
    def get_list():
        lines = Line.objects.all()
        return lines


class GenericLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Line
        fields = '__all__'

class GenericCitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'

class GenericContainerGetSerializer(serializers.ModelSerializer):
    iamge = serializers.SerializerMethodField()
    class Meta:
        model = Container
        fields = '__all__'

    def get_image(self, image):
        try:
            request = self.context.get('request')
            photo_url = image.image_png.url
            return request.build_absolute_uri(photo_url)
        except Exception:
            return None
class GenericContainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Container
        fields = '__all__'

