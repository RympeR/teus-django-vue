from django.http import request
from rest_framework import generics, permissions, filters, parsers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City, Container, Line
from .serializers import (
    CitySerializer, ContainerSerializer, LineSerializer,
    GenericLineSerializer, GenericCitySerializer, GenericContainerSerializer,
    GenericContainerGetSerializer
)
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import permission_classes, renderer_classes, api_view, parser_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

@renderer_classes((JSONRenderer,))
@permission_classes((permissions.AllowAny,))
class OldContainerAPI(APIView):
    parser_classes = (MultiPartParser,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get(self, *args, **kwargs):
        container = ContainerSerializer.get(**kwargs)
        domain = self.request.get_host()
        path_image = container.image.url
        image_url = 'http://{domain}{path}'.format(
            domain=domain, path=path_image)
        return Response(
            {
                "container_id": container.id,
                "name": container.name,
                "image": image_url,
            }
        )

    def post(self, *args, **kwargs):
        container_id = ContainerSerializer.post(self.request.data)
        return Response(
            {
                "container_id": container_id
            }
        )

    def put(self, *args, **kwargs):
        data = dict(self.request.data)
        data['container_id'] = kwargs['container_id']
        container = ContainerSerializer.put(data)
        domain = self.request.get_host()
        path_image = container.image.url
        image_url = 'http://{domain}{path}'.format(
            domain=domain, path=path_image)
        print(image_url)
        return Response(
            {
                "container_id": container.id,
                "name": container.name,
                "image": image_url,
            }
        )

    def delete(self, request, container_id):
        container = ContainerSerializer.delete(container_id)
        return Response(
            {
                "container_id": container_id
            }
        )


@api_view(['GET'])
@parser_classes((MultiPartParser, ))
@renderer_classes((JSONRenderer,))
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
@permission_classes((permissions.AllowAny,))
def get_containers_list(request):
    containers = ContainerSerializer.get_list()
    containers_list = containers.values()
    domain = request.get_host()
    for ind, container in enumerate(containers_list):
        path_image = containers[ind].image.url
        image_url = 'http://{domain}{path}'.format(
            domain=domain, path=path_image)
        containers_list[ind]['image'] = image_url

    return Response(
        {
            "results": containers_list
        }
    )


@api_view(['GET'])
@parser_classes((MultiPartParser, ))
@renderer_classes((JSONRenderer,))
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
@permission_classes((permissions.AllowAny,))
def get_containers_list_api(request):
    containers = ContainerSerializer.get_list()
    containers_list = containers.values()
    domain = request.get_host()
    for ind, container in enumerate(containers_list):
        path_image = containers[ind].image.url
        image_url = 'http://{domain}{path}'.format(
            domain=domain, path=path_image)
        containers_list[ind]['image'] = image_url
    return Response(
        containers_list
    )


@renderer_classes((JSONRenderer,))
@permission_classes((permissions.AllowAny,))
class OldCityAPI(APIView):
    parser_classes = (MultiPartParser,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get(self, *args, **kwargs):
        city = CitySerializer.get(**kwargs)
        return Response(
            {
                "city_id": city.id,
                "name": city.name
            }
        )

    def post(self, *args, **kwargs):
        print(self.request.data)
        city_id = CitySerializer.post(self.request.data)
        return Response(
            {
                "city_id": city_id
            }
        )

    def put(self, *args, **kwargs):
        data = dict(self.request.data)
        data['city_id'] = kwargs['city_id']
        city = CitySerializer.put(data)
        return Response(
            {
                "city_id": city.id,
                "name": city.name,
            }
        )

    def delete(self, *args, **kwargs):
        city = CitySerializer.delete(**kwargs)
        return Response(
            {
                "city_id": city[0]
            }
        )


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
@parser_classes((MultiPartParser, ))
@permission_classes((permissions.AllowAny,))
def get_cities_list_api(request):
    cities = CitySerializer.get_list()
    cities_list = cities.values()

    return Response(
        cities_list
    )


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
@parser_classes((MultiPartParser, ))
@permission_classes((permissions.AllowAny,))
def get_cities_list(request):
    cities = CitySerializer.get_list()
    cities_list = cities.values()

    return Response(
        {
            "results": cities_list
        }
    )


@renderer_classes((JSONRenderer,))
@permission_classes((permissions.AllowAny,))
class OldLineAPI(APIView):
    parser_classes = (MultiPartParser,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get(self, *args, **kwargs):
        line = LineSerializer.get(**kwargs)
        return Response(
            {
                "line_id": line.id,
                "name": line.name
            }
        )

    def post(self, *args, **kwargs):
        line_id = LineSerializer.post(self.request.data)
        return Response(
            {
                "line_id": line_id
            }
        )

    def put(self, *args, **kwargs):
        data = dict(self.request.data)
        data['line_id'] = kwargs['line_id']
        line = LineSerializer.put(data)
        return Response(
            {
                "line_id": line.id,
                "name": line.name
            }
        )

    def delete(self, *args, **kwargs):
        line = LineSerializer.delete(**kwargs)
        return Response(
            {
                "line_id": line[0]
            }
        )


@api_view(['GET'])
@parser_classes((MultiPartParser, ))
@renderer_classes((JSONRenderer,))
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
@permission_classes((permissions.AllowAny,))
def get_lines_list(request):
    lines = LineSerializer.get_list()
    lines_list = lines.values()

    return Response(
        {
            "results": lines_list
        }
    )


@api_view(['GET'])
@parser_classes((MultiPartParser, ))
@renderer_classes((JSONRenderer,))
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
@permission_classes((permissions.AllowAny,))
def get_lines_list_api(request):
    lines = LineSerializer.get_list()
    lines_list = lines.values()

    return Response(
        lines_list
    )


class LineAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Line.objects.all()
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)
    serializer_class = GenericLineSerializer

class CreateLineAPI(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Line.objects.all()
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)
    serializer_class = GenericLineSerializer

class CityAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = City.objects.all()
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)
    serializer_class = GenericCitySerializer

class CreateCityAPI(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = City.objects.all()
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)
    serializer_class = GenericCitySerializer

class ContainerAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Container.objects.all()
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)
    serializer_class = GenericContainerGetSerializer

class CreateContainerAPI(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Container.objects.all()
    parser_classes = (parsers.JSONParser, parsers.MultiPartParser, parsers.FormParser)
    serializer_class = GenericContainerSerializer

