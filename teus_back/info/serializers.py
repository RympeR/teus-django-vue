from rest_framework import serializers
from .models import City, Container, Line
from django.db.models import Q
from django.shortcuts import get_object_or_404
import ast


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = (
            'id',
            'name'
        )

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
        fields = (
            'id',
            'name',
            'image'
        )

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
        container.save()
        try:
            container.image = validated_data['image'][0]
        except KeyError:
            container.image = container.image
        return container

    @staticmethod
    def delete(container_id):
        container = get_object_or_404(Container, pk=container_id)
        try:
            container = container.delete()
        except Exception:
            pass
        return container

    @staticmethod
    def get_list():
        containers = Container.objects.all()
        return containers


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Line
        fields = (
            'id',
            'name'
        )

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
