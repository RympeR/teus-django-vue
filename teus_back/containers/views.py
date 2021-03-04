from django.shortcuts import render
from .models import *
from .serializers import DealSerializer, RequestSerializer, PropositionSerializer
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
from django.core.paginator import Paginator
import locale
from datetime import date

class RequestAPI(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )

    def get(self, request, request_id):
        user_request = RequestSerializer.get_request(request_id)
        return Response(
            {
                "id": user_request.id,
                "name": user_request.user.first_name,
                "phone": user_request.user.phone,
                "amount": user_request.amount,
                "city": user_request.city.name,
                "line": user_request.line.name,
                "container": user_request.container.name,
                "request_date": user_request.request_date.strftime('%d %B %Y'),
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
                "name": proposition.user.first_name,
                "phone": proposition.user.phone,
                "amount": proposition.amount,
                "city": proposition.city.name,
                "line": proposition.line.name,
                "container": proposition.container.name,
                "start_date": proposition.start_date.strftime('%d %B %Y')
,
                "end_date": proposition.end_date.strftime('%d %B %Y')

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


class DealAPI(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )

    def get(self, request, deal_id):
        deal = DealSerializer.get_deal(deal_id)
        return Response(
            {
                "id": deal.id,
                "user_request": deal.user_request.phone,
                "user_request_name": deal.user_request.first_name,
                "user_proposition": deal.user_proposition.phone,
                "user_proposition_name": deal.user_proposition.first_name,
                "amount": deal.amount,
                "city": deal.city.name,
                "line": deal.line.name,
                "container": deal.container.name,
                "handshake_time": deal.handshake_time.strftime('%H:%M:%S %d %b %Y'),
            }
        )
    
    def post(self, request):
        deal = DealSerializer(data=request.data)
        if deal.is_valid():
            deal.save()
            deal = Deal.objects.get(
                pk=request.data['id'])
            return Response({
                "id": deal.id
            })
        else:
            print(deal)
            return Response({
                "id": "0"
            })


    def get_object(self, deal_id):
        return Deal.objects.get(pk=deal_id)

    def put(self, requset, deal_id):
        instance = self.get_object(deal_id)
        deal = DealSerializer(instance)
        data = deal.update()
        return Response(
            {
                "data": data
            }
        )
    
    def delete(self, request, deal_id):
        deal_id = DealSerializer.delete_deal(deal_id)
        
        return Response(
            {
                "id": deal_id
            }
        )

def datetowords(string):
    day_, month_, year_ = [int(i) for i in reversed(string.split('-'))]
    return date(day=day_, month=month_, year=year_).strftime('%d %B %Y')


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
                    "name": row[4],
                    "phone": row[5]
                },
                "line": {
                    "id": row[6],
                    "name": row[7]
                },
                "container": {
                    "id": row[8],
                    "name": row[9]
                },
                "amount": row[10],
                "date": row[11].strftime('%d %B %Y')

            })
        return Response(
            {
                "results":result['results']
            }
        )


class PropositionList(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    userfilter = UserFilter()

    def get(self, request):
        data = self.userfilter.get_propositions(request, 'postgres', '1111')
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
                    "name": row[4],
                    "phone": row[5]
                },
                "line": {
                    "id": row[6],
                    "name": row[7]
                },
                "container": {
                    "id": row[8],
                    "name": row[9]
                },
                "amount": row[10],
                "date": {
                    "start": row[11].strftime('%d %B %Y'),
                    "end": row[12].strftime('%d %B %Y')
                }
            })
        return Response(
            {
                "results":result['results']
            }
        )

class DealsList(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    userfilter = UserFilter()

    def get(self, request):
        print(request.GET)
        data = self.userfilter.get_deals(request, 'postgres', '1111')
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
                "first_user": {
                    "id": row[3],
                    "name": row[4],
                    "phone": row[5]
                },
                "second_user": {
                    "id": row[6],
                    "name": row[7],
                    "phone": row[8]
                },
                "line": {
                    "id": row[9],
                    "name": row[10]
                },
                "container": {
                    "id": row[11],
                    "name": row[12]
                },
                "amount": row[13],
                "handshake_time": row[14].strftime('%H:%M:%S %d %b %Y')

            })
        return Response(
            {
                "results":result['results']
            }
        )
