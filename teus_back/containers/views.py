from django.shortcuts import render
from .models import *
from .serializers import RequestSerializer, PropositionSerializer
from django.http import request
from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import permission_classes, renderer_classes, api_view, parser_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .raw_sql import UserFilter


class RequestAPI(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )

    def get(self, request, request_id):
        user_request = RequestSerializer.get_request(request_id)
        return Response(
            {
                "id": user_request.id,
                "phone": user_request.user.phone,
                "amount": user_request.amount,
                "city": user_request.city.name,
                "line": user_request.line.name,
                "container": user_request.container.name,
                "request_date": user_request.request_date,
            }
        )

    def post(self, request):
        user_request = RequestSerializer(data=request.data)
        if user_request.is_valid():
            user_request.save()
            user_request = UserRequest.objects.get(pk=request.data['id'])
            return Response({
                "id": user_request.id
            })

    def delete(self, request, request_id):
        request_id = RequestSerializer.delete(request_id)
        return Response(
            {
                "id": request_id
            }
        )


class RequestUpdateAPI(generics.UpdateAPIView):
    queryset = UserRequest.objects.all()
    serializer_class = RequestSerializer

    def get_queryset(self):
        user = self.request.user
        return user.accounts.all()

    def get_object(self, queryset=None):
        # instead of self.request.GET or self.request.POST
        obj = self.model.objects.get(my_id_or_name_of_field=self.kwargs['pk'])
        return obj

    def perform_update(self, serializer):
        instance = serializer.save()
        print(instance)


class PropositionAPI(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )

    def get(self, request, proposition_id):
        proposition = PropositionSerializer.get_propos(proposition_id)
        return Response(
            {
                "id": proposition.id,
                "phone": proposition.user.phone,
                "amount": proposition.amount,
                "city": proposition.city.name,
                "line": proposition.line.name,
                "container": proposition.container.name,
                "start_date": proposition.start_date,
                "end_date": proposition.end_date
            }
        )

    def post(self, request):
        user_proposition = PropositionSerializer(data=request.data)
        if user_proposition.is_valid():
            user_proposition.save()
            user_proposition = UserProposition.objects.get(
                pk=request.data['id'])
            return Response({
                "id": user_proposition.id
            })

    def put(self, request, proposition_id):
        instance = self.get_object(proposition_id)
        proposition = PropositionSerializer(instance)
        data = proposition.update()
        return Response(
            {
                "data": data
            }
        )

    def get_object(self, proposition_id):
        return UserProposition.objects.get(pk=proposition_id)

    def delete(self, request, proposition_id):
        proposition_id = PropositionSerializer.delete(proposition_id)
        return Response(
            {
                "id": proposition_id
            }
        )


class RequestsList1(generics.ListAPIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    queryset = UserRequest.objects.all()
    serializer_class = RequestSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__phone', '=city__name',
                     '=line__name', 'amount', '=container__name', '^request_date']

    def get_queryset(self):
        queryset = self.filter_queryset(UserRequest.objects.all())

        return queryset


class PropositionList1(generics.ListAPIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    queryset = UserProposition.objects.all()
    serializer_class = PropositionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__phone', '=city__name',
                     '=line__name', 'amount', '=container__name', '^end_date']

    def filter_queryset(self, queryset):
        filter_backends = [filters.SearchFilte]
        if 'geo_route' in self.request.query_params:
            ...
        for backend in list(filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, view=self)

        return queryset

    def get_queryset(self):
        queryset = self.filter_queryset(UserProposition.objects.all())
        return queryset


class RequestsList(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    userfilter = UserFilter()

    def get(self, request):
        print(request.GET)
        data = self.userfilter.get_requests(request, 'postgres', '1111')
        result = {
            "results": []
        }
        for ind, row in enumerate(data):
            result['results'].append({
                "id": row[0],
                "city": {
                    "id": row[1],
                    "name": row[2]
                },
                "user": {
                    "id": row[3],
                    "phone": row[4]
                },
                "line": {
                    "id": row[5],
                    "name": row[6]
                },
                "container": {
                    "id": row[7],
                    "name": row[8]
                },
                "amount": row[9],
                "date": row[10]

            })
        return Response(result)


class PropositionList(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    userfilter = UserFilter()

    def get(self, request):
        data = self.userfilter.get_propositions(request, 'postgres', '1111')
        result = {
            "result": []
        }
        for ind, row in enumerate(data):
            result['result'].append({
                "city": {
                    "id": row[0],
                    "name": row[1]
                },
                "user": {
                    "id": row[2],
                    "phone": row[3]
                },
                "line": {
                    "id": row[4],
                    "name": row[5]
                },
                "container": {
                    "id": row[6],
                    "name": row[7]
                },
                "amount": row[8],
                "date": {
                    "start": row[9],
                    "end": row[10]
                }
            })
        return Response(result)
