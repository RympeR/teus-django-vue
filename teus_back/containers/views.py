from .models import *
from django.shortcuts import render
from .serializers import DealSerializer, RequestSerializer, PropositionSerializer
from django.http import request
from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import permission_classes, renderer_classes, api_view, parser_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .raw_sql import UserFilter
from django.core.paginator import Paginator
import locale
from datetime import date
from users.models import *
from info.models import *


class RequestAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer,)
    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def get(self, request, request_id):
        try:
            user = User.objects.get(token=self.request.headers['token'])
        except Exception:
            user = None
        if user:
            user_request = RequestSerializer.get_request(request_id)
            return Response(
                {
                    "id": user_request.id,
                    "user": {
                        "id": user_request.user.id,
                        "name": user_request.user.first_name,
                        "phone": user_request.user.phone
                    },
                    "amount": user_request.amount,
                    "city": {
                        "id": user_request.city.id,
                        "name": user_request.city.name,
                    },
                    "container": {
                        "id": user_request.container.id,
                        "name": user_request.container.name,
                    },
                    "line": {
                        "id": user_request.line.id,
                        "name": user_request.line.name,
                    },
                    "request_date": user_request.request_date,
                    "end_date": user_request.end_date
                }
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )

    def post(self, request):
        try:
            user = User.objects.get(token=self.request.headers['token'])
        except Exception:
            user = None
        if user:
            user_request = RequestSerializer(data=request.data)
            if user_request.is_valid():
                user_request.save()
                return Response({
                    "id": user_request.data['id']
                })
            else:
                return Response(
                    user_request.data
                )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )

    def get_object(self, request_id):
        return UserRequest.objects.get(pk=request_id)

    def put(self, request, request_id):
        try:
            user = User.objects.get(token=self.request.headers['token'])
        except Exception:
            user = None
        if user:
            instance = self.get_object(request_id)
            user_request = RequestSerializer(
                instance=instance, data=request.data)
            if user_request.is_valid():
                user_request.save()
                return Response({
                    "id": user_request.data['id']
                })
            else:
                return Response(
                    user_request.data
                )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )

    def delete(self, request, request_id):
        try:
            user = User.objects.get(token=self.request.headers['token'])
        except Exception:
            user = None
        if user:
            request_obj = RequestSerializer.delete(request_id)
            return Response(
                {
                    "id": request_id
                }
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )


class PropositionAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer,)
    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def get(self, request, proposition_id):
        try:
            user = User.objects.get(token=self.request.headers['token'])
        except Exception:
            user = None
        if user:
            proposition = PropositionSerializer.get_propos(proposition_id)
            return Response(
                {
                    "id": proposition.id,
                    "user": {
                        "id": proposition.user.id,
                        "name": proposition.user.first_name,
                        "phone": proposition.user.phone
                    },
                    "amount": proposition.amount,
                    "city": {
                        "id": proposition.city.id,
                        "name": proposition.city.name,
                    },
                    "container": {
                        "id": proposition.container.id,
                        "name": proposition.container.name,
                    },
                    "line": {
                        "id": proposition.line.id,
                        "name": proposition.line.name,
                    },
                    "start_date": proposition.start_date
                }
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )

    def post(self, request):
        try:
            user = User.objects.get(token=self.request.headers['token'])
        except Exception:
            user = None
        if user:
            user_proposition = PropositionSerializer(data=request.data)
            if user_proposition.is_valid():
                user_proposition.save()
                return Response({
                    "id": user_proposition.data['id']
                })
            else:
                return Response(
                    user_proposition.data
                )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )

    def put(self, request, proposition_id):
        try:
            user = User.objects.get(token=self.request.headers['token'])
        except Exception:
            user = None
        if user:
            instance = self.get_object(proposition_id)
            user_proposition = PropositionSerializer(
                instance=instance, data=request.data)
            if user_proposition.is_valid():
                user_proposition.save()
                return Response({
                    "id": user_proposition.data['id']
                })
            else:
                return Response(
                    user_proposition.data
                )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )

    def get_object(self, proposition_id):
        return UserProposition.objects.get(pk=proposition_id)

    def delete(self, request, proposition_id):
        try:
            user = User.objects.get(token=self.request.headers['token'])
        except Exception:
            user = None
        if user:
            proposition_obj = PropositionSerializer.delete(proposition_id)
            return Response(
                {
                    "id": proposition_id
                }
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )


class DealAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer,)
    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def get(self, request, deal_id):
        try:
            user = User.objects.get(token=self.request.headers['token'])
        except Exception:
            user = None
        if user:
            deal = DealSerializer.get_deal(deal_id)

            return Response(
                {
                    "id": deal.id,
                    "first_user": {
                        "id": deal.user_request.id,
                        "name": deal.user_request.first_name,
                        "phone": deal.user_request.phone
                    },
                    "sec_user": {
                        "id": deal.user_proposition.id,
                        "name": deal.user_proposition.first_name,
                        "phone": deal.user_proposition.phone
                    },
                    "amount": deal.amount,
                    "city": {
                        "id": deal.city.id,
                        "name": deal.city.name,
                    },
                    "container": {
                        "id": deal.container.id,
                        "name": deal.container.name,
                    },
                    "line": {
                        "id": deal.line.id,
                        "name": deal.line.name,
                    },
                    "amount": deal.amount,
                    "handshake": {
                        "handshake": deal.handshake_time.strftime('%H:%M:%S %d %b %Y'),
                        "raw_handshake": deal.handshake_time
                    }
                }
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )

    def post(self, request):
        try:
            user = User.objects.get(token=self.request.headers['token'])
        except Exception:
            user = None
        if user:
            deal = DealSerializer(data=request.data)
            if deal.is_valid():
                deal.save()
                return Response({
                    "id": deal.data['id']
                })
            else:
                print(deal.data)
                return Response({
                    "id": deal.data
                })
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )

    def get_object(self, deal_id):
        return Deal.objects.get(pk=deal_id)

    def put(self, request, deal_id=None):
        try:
            user = User.objects.get(token=self.request.headers['token'])
        except Exception:
            user = None
        if user:
            instance = self.get_object(deal_id)
            deal = DealSerializer(instance=instance, data=request.data)
            if deal.is_valid():
                deal.save()
                return Response({
                    "id": deal.data['id']
                })
            else:
                print(deal.data)
                return Response({
                    "id": deal.data
                })
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )

    def delete(self, request, deal_id):
        try:
            user = User.objects.get(token=self.request.headers['token'])
        except Exception:
            user = None
        if user:
            deal_obj = DealSerializer.delete_deal(deal_id)

            return Response(
                {
                    "id": deal_id
                }
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )


locale.setlocale(locale.LC_TIME, "rus")


def datetowords(string):
    day_, month_, year_ = [int(i) for i in reversed(string.split('-'))]
    return date(day=day_, month=month_, year=year_).strftime('%d %B %Y')


class RequestsList(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    userfilter = UserFilter()

    def get(self, request):
        try:
            user = User.objects.get(token=self.request.headers['token'])
        except Exception:
            user = None
        if user:
            data = self.userfilter.get_requests(request, 'postgres', '1111')
        else:
            request.GET = {}
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
                "date": {
                    "start": row[11].strftime('%d %B %Y'),
                    "end": row[12].strftime('%d %B %Y')
                }


            })
        return Response(
            {
                "results": result['results']
            }
        )


class PropositionList(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    userfilter = UserFilter()

    def get(self, request):
        try:
            user = User.objects.get(token=self.request.headers['token'])
        except Exception:
            user = None
        if user:
            data = self.userfilter.get_propositions(
                request, 'postgres', '1111')
        else:
            request.GET = {}
            data = self.userfilter.get_propositions(
                request, 'postgres', '1111')
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
                "results": result['results']
            }
        )


class DealsList(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    userfilter = UserFilter()

    def get(self, request):

        try:
            user = User.objects.get(token=self.request.headers['token'])
        except Exception:
            user = None
        if user:
            data = self.userfilter.get_deals(request, 'postgres', '1111')
        else:
            request.GET = {}
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
                "sec_user": {
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
                "handshake": row[14].strftime('%H:%M:%S %d %b %Y')

            })
        return Response(
            {
                "results": result['results']
            }
        )
