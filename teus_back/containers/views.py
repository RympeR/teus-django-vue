from .models import *
from chat.models import *
from django.shortcuts import render
from .serializers import (
    DealSerializer, RequestSerializer,GenericUpdateRequestSerializer,
    PropositionSerializer, UserPropositionsSerializer,GenericUpdatePropositionSerializer,
    UserRequsetSerializer, GenericRequestSerializer, GetGenericRequestSerializer, GenericPropositionSerializer, GetGenericPropositionSerializer)
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
from datetime import datetime
from datetime import date
from users.models import *
from info.models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status
from django.db.models import Q
from pprint import pprint
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
import logging
logger = logging.getLogger('django')


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


class RequestAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer,)
    parser_classes = (MultiPartParser, FormParser, JSONParser, )
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request, request_id):
        try:
            user = User.objects.get(
                token=request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            user_request = RequestSerializer.get_request(request_id)
            city_result = []
            for city in user_request.city.all():
                city_result.append({
                    "id": city.id,
                    "name": city.name,
                })

            return Response(
                {
                    "id": user_request.id,
                    "user": {
                        "id": user_request.user.id,
                        "name": user_request.user.first_name,
                        "phone": user_request.user.phone
                    },
                    "amount": user_request.amount,
                    "city": city_result,
                    "container": {
                        "id": user_request.container.id,
                        "name": user_request.container.name,
                    },
                    "line": {
                        "id": user_request.line.id,
                        "name": user_request.line.name,
                    },
                    "request_date": int(user_request.request_date.timestamp()),
                    "end_date": int(user_request.end_date.timestamp()),
                    "status": user_request.get_status_display(),
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
            user = User.objects.get(
                token=self.request.headers['Authorization'])
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
            user = User.objects.get(
                token=self.request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            instance = self.get_object(request_id)
            user_request = RequestSerializer(
                instance=instance, data=self.request.data)
            print(user_request)
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
            user = User.objects.get(
                token=self.request.headers['Authorization'])
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
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request, proposition_id):
        try:
            user = User.objects.get(
                token=self.request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            proposition = PropositionSerializer.get_propos(proposition_id)
            from datetime import datetime
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
                    "start_date": int(proposition.start_date.timestamp()),
                    "end_date": int(proposition.end_date.timestamp()),
                    "created_at": int(proposition.created_at.timestamp()),
                    "status": proposition.get_status_display(),
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
            user = User.objects.get(
                token=self.request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            user_proposition = PropositionSerializer(data=request.data)
            if user_proposition.is_valid():
                user_proposition.save()
                response = Response({
                    "id": user_proposition.data['id']
                })
                response["Access-Control-Allow-Origin"] = 'Authorization'
                return response
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
            user = User.objects.get(
                token=self.request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            instance = self.get_object(proposition_id)
            user_proposition = PropositionSerializer(
                instance=instance, data=request.data)
            print(user_proposition)
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
            user = User.objects.get(
                token=self.request.headers['Authorization'])
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
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request, deal_id):
        try:
            user = User.objects.get(
                token=self.request.headers['Authorization'])
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
            user = User.objects.get(
                token=self.request.headers['Authorization'])
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
            user = User.objects.get(
                token=self.request.headers['Authorization'])
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
            user = User.objects.get(
                token=self.request.headers['Authorization'])
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


locale.setlocale(locale.LC_TIME, "ru_RU.utf8")
#locale.setlocale(locale.LC_TIME, "ru")


def datetowords(string):
    day_, month_, year_ = [int(i) for i in reversed(string.split('-'))]
    return date(day=day_, month=month_, year=year_).strftime('%d %B %Y')


class RequestsAPIList(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    userfilter = UserFilter()
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request):
        data = self.userfilter.get_requests(request, 'teus_dev', 'teus_dev')
        try:
            user = User.objects.get(
                token=self.request.headers['Authorization'])
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
                    "name": ', '.join(row[1])
                },
                "user": {
                    "id": row[2],
                    "name": row[3],
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
                "date": {
                    "start": row[10].strftime('%d %B %Y'),
                    "end": row[11].strftime('%d %B %Y')
                },
                "status": row[12]

            })
        return Response(
            result['results']
        )


class RequestsList(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    userfilter = UserFilter()
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request):
        data = self.userfilter.get_requests(request, 'teus_dev', 'teus_dev')
        try:
            user = User.objects.get(
                token=self.request.headers['Authorization'])
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
                    "name": ', '.join(row[1])
                },
                "user": {
                    "id": row[2],
                    "name": row[3],
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
                "date": {
                    "start": row[10],
                    "end": row[11]
                },
                "status": row[12]

            })
        return Response(
            {
                "results": result['results']
            }
        )


class PropositionAPIList(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    userfilter = UserFilter()

    def get(self, request):
        data = self.userfilter.get_propositions(
            request, 'teus_dev', 'teus_dev')
        try:
            user = User.objects.get(
                token=self.request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            data = self.userfilter.get_propositions(
                request, 'postgres', '1111')
        else:
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
                "date": {
                    "start": row[11].strftime('%d %B %Y'),
                    "end": row[12].strftime('%d %B %Y')
                },
                "status": row[13]
            })
        return Response(
            result['results']
        )


class PropositionList(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    userfilter = UserFilter()

    def get(self, request):
        data = self.userfilter.get_propositions(
            request, 'teus_dev', 'teus_dev')
        try:
            user = User.objects.get(
                token=self.request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            data = self.userfilter.get_propositions(
                request, 'postgres', '1111')
        else:
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
                "date": {
                    "start": row[11],
                    "end": row[12]
                },
                "status": row[13]
            })
        return Response(
            {
                "results": result['results']
            }
        )


class DealsAPIList(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    userfilter = UserFilter()
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request):
        data = self.userfilter.get_deals(request, 'teus_dev', 'teus_dev')

        try:
            user = User.objects.get(
                token=self.request.headers['Authorization'])
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
                "handshake": row[14].strftime('%H:%M:%S %d %b %Y'),
            })
        return Response(
            result['results']
        )


class DealsList(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    userfilter = UserFilter()
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request):
        data = self.userfilter.get_deals(request, 'teus_dev', 'teus_dev')

        try:
            user = User.objects.get(
                token=self.request.headers['Authorization'])
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
                "handshake": row[14],
            })
        return Response(
            {
                "results": result['results']
            }
        )


class APIDOCUserRequests(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def get(self, request):
        try:
            user = User.objects.get(
                token=request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            if request.GET.get('is_active') == '1':
                user_requests = UserRequest.objects.filter(
                    user=user, status='в работе'
                )
            else:
                user_requests = UserRequest.objects.filter(
                    user=user, status='в архиве'
                )
            limit = int(request.GET.get('limit', 20))
            offset = int(request.GET.get('offset', 0))
            result = []
            domain = request.get_host()

            for request_ in user_requests:

                try:
                    path_image = request_.user.image.url
                except Exception:
                    path_image = None
                if path_image:
                    image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=path_image)
                else:
                    image_url = None
                try:
                    container_image = request_.container.image.url
                except Exception:
                    container_image = None
                if container_image:
                    container_image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=container_image)
                else:
                    container_image_url = None
                city_result = []
                for city in request_.city.all():
                    city_result.append({
                        "id": city.id,
                        "name": city.name,
                    })
                rooms = Room.objects.filter(request_id=request_)
                for room in rooms:
                    if not room.request_user_readed:
                        readed = False
                        break
                else:
                    readed = True
                result.append(
                    {
                        "id": request_.id,
                        "user": {
                            "id": request_.user.id,
                            "name": request_.user.first_name,
                            "phone": request_.user.phone,
                            "onesignal_token": request_.user.onesignal_token,
                            "image": image_url
                        },
                        "amount": request_.amount,
                        "city": city_result,
                        "container": {
                            "id": request_.container.id,
                            "name": request_.container.name,
                            "image": container_image_url
                        },
                        "line": {
                            "id": request_.line.id,
                            "name": request_.line.name,
                        },
                        "readed": readed,
                        "status": request_.status,
                        "request_date": int(request_.request_date.timestamp()),
                        "end_date": int(request_.end_date.timestamp()),
                    }
                )
            return Response(
                result[offset: offset+limit]
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )


class UserRequestsAPI(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def get(self, request):
        try:
            user = User.objects.get(
                token=request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            user_requests = UserRequest.objects.filter(
                user=user
            )
            result = []
            domain = request.get_host()
            for request_ in user_requests:
                try:
                    path_image = request_.user.image.url
                except Exception:
                    path_image = None
                if path_image:
                    image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=path_image)
                else:
                    image_url = None
                container_image = request_.container.image.url
                container_image_url = 'http://{domain}{path}'.format(
                    domain=domain, path=container_image)
                city_result = []
                for city in request_.city.all():
                    city_result.append({
                        "id": city.id,
                        "name": city.name,
                    })
                from datetime import datetime
                result.append(
                    {
                        "id": request_.id,
                        "user": {
                            "id": request_.user.id,
                            "name": request_.user.first_name,
                            "phone": request_.user.phone,
                            "image": image_url
                        },
                        "amount": request_.amount,
                        "city": city_result,
                        "container": {
                            "id": request_.container.id,
                            "name": request_.container.name,
                            "image": container_image_url
                        },
                        "line": {
                            "id": request_.line.id,
                            "name": request_.line.name,
                        },
                        "status": request_.get_status_display(),
                        "request_date": int(request_.request_date),
                        "end_date": int(request_.end_date),
                    }
                )
            return Response({
                "results": result

            })
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )

    def post(self, request):
        try:
            user = User.objects.get(
                token=self.request.headers['Authorization'])
        except Exception:
            user = None
        except TypeError:
            user = None
        if user:
            from datetime import datetime
            data = dict(request.data)

            data['user'] = user.id
            if isinstance(data['request_date'], list):
                data['request_date'] = int(data['request_date'][0])
            if isinstance(data['end_date'], list):
                data['end_date'] = int(data['end_date'][0])
            data['request_date'] = datetime.utcfromtimestamp(
                data['request_date']).strftime("%Y-%m-%d")
            data['end_date'] = datetime.utcfromtimestamp(
                data['end_date']).strftime("%Y-%m-%d")
            user_request = UserRequsetSerializer(data=data)
            if user_request.is_valid():
                user_request.save()
                return Response({
                    "id": user_request.data['id']
                })
            else:
                return Response(
                    user_request.data,
                    status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )

    def put(self, request):
        try:
            user = User.objects.get(
                token=self.request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            user_request = UserRequest.objects.get(pk=request.data['id'])
            user_request.status = request.data['status']
            user_request.save()
            return Response(
                {
                    "id": user_request.id,
                    "status": user_request.get_status_display()
                }
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )


class APDICOUserPropositionsAPI(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def get(self, request):
        try:
            user = User.objects.get(
                token=request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            if request.GET.get('is_active') == '1':
                user_propositions = UserProposition.objects.filter(
                    user=user, status='в работе'
                )
            else:
                user_propositions = UserProposition.objects.filter(
                    user=user, status='в архиве'
                )

            limit = int(request.GET.get('limit', 20))
            offset = int(request.GET.get('offset', 0))
            result = []
            domain = request.get_host()
            for proposition in user_propositions:
                try:
                    path_image = proposition.user.image.url
                except Exception:
                    path_image = None
                if path_image:
                    image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=path_image)
                else:
                    image_url = None
                try:
                    container_image = proposition.container.image.url
                except Exception:
                    container_image = None
                if container_image:
                    container_image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=container_image)
                else:
                    container_image_url = None
                rooms = Room.objects.filter(proposition_id=proposition)
                for room in rooms:
                    if not room.proposition_user_readed:
                        readed = False
                        break
                else:
                    readed = True
                result.append(
                    {
                        "id": proposition.id,
                        "user": {
                            "id": proposition.user.id,
                            "name": proposition.user.first_name,
                            "phone": proposition.user.phone,
                            "image": image_url
                        },
                        "amount": proposition.amount,
                        "city": {
                            "id": proposition.city.id if proposition.city else None,
                            "name": proposition.city.name if proposition.city else None,
                        },
                        "container": {
                            "id": proposition.container.id,
                            "name": proposition.container.name,
                            "image": container_image_url

                        },
                        "line": {
                            "id": proposition.line.id if proposition.line else None,
                            "name": proposition.line.name if proposition.line else None,
                        },
                        "readed": readed,
                        "status": proposition.status,
                        "created_at": int(proposition.created_at.timestamp()),
                        "start_date": int(proposition.start_date.timestamp()),
                        "end_date": int(proposition.end_date.timestamp())
                    }
                )
            print(result)
            return Response(
                result[offset:limit+offset]
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )


class UserPropositionsAPI(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def get(self, request):
        try:
            user = User.objects.get(
                token=request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            user_propositions = UserProposition.objects.filter(
                user=user
            )
            result = []
            domain = request.get_host()
            for proposition in user_propositions:
                try:
                    path_image = proposition.user.image.url
                except Exception:
                    path_image = None
                if path_image:
                    image_url = 'http://{domain}{path}'.format(
                        domain=domain, path=path_image)
                else:
                    image_url = None
                container_image = proposition.container.image.url
                container_image_url = 'http://{domain}{path}'.format(
                    domain=domain, path=container_image)
                result.append(
                    {
                        "id": proposition.id,
                        "user": {
                            "id": proposition.user.id,
                            "name": proposition.user.first_name,
                            "phone": proposition.user.phone,
                            "image": image_url
                        },
                        "amount": proposition.amount,
                        "city": {
                            "id": proposition.city.id,
                            "name": proposition.city.name,
                        },
                        "container": {
                            "id": proposition.container.id,
                            "name": proposition.container.name,
                            "image": container_image_url
                        },
                        "line": {
                            "id": proposition.line.id,
                            "name": proposition.line.name,
                        },
                        "start_date": int(proposition.start_date.timestamp()),
                        "end_date": int(proposition.end_date.timestamp())
                    }
                )
            return Response({
                "result": result

            })
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )

    def put(self, request):
        try:
            user = User.objects.get(
                token=self.request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            user_proposition = UserProposition.objects.get(
                pk=request.data['id'])
            user_proposition.status = request.data['status']
            user_proposition.save()
            return Response(
                {
                    "id": user_proposition.id,
                    "status": user_proposition.status
                }
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )


class GetOutOfChat(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def get(self, request, pk):
        try:

            user = User.objects.get(
                token=request.headers['Authorization'])
        except Exception:
            user = None

        if user:
            room = Room.objects.get(pk=pk)
            logger.warning(user)
            logger.warning(room.request_id.user == user)
            logger.warning(room.proposition_id.user == user)
            if room.request_id.user == user:
                room.request_user_readed = True
                room.save()
            if room.proposition_id.user == user:
                room.proposition_user_readed = True
                room.save()
            room.save()
            return Response({
                "user": user.pk,
                "readed": True
            })
        else:
            return Response({
                "status": "No token specified"
            })


class FilteredPropositions(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def get(self, request):
        try:

            limit = int(request.GET.get('limit', 20))
            offset = int(request.GET.get('offset', 0))
            deals = None
            user = User.objects.get(
                token=request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            if request.GET.get('id', None):
                _filter = UserRequest.objects.get(
                    pk=request.GET['id']
                )

                propositons = UserProposition.objects.filter(
                    Q(status='в работе') &
                    Q(city__name__in=_filter.city.all().values('name')) &
                    Q(container__name__contains=_filter.container.name) &
                    (
                        (
                            Q(start_date__gte=_filter.request_date) &
                            Q(start_date__lte=_filter.end_date) &
                            Q(end_date__gte= _filter.end_date)
                        ) |
                        (
                            Q(start_date__gte=_filter.request_date) &
                            Q(end_date__lte=_filter.end_date)
                        ) |
                        (
                            Q(start_date__lte=_filter.request_date) &
                            Q(end_date__lte=_filter.end_date) &
                            Q(end_date__gte= _filter.request_date)
                        ) |
                        (
                            Q(start_date__lte=_filter.request_date) &
                            Q(end_date__gte= _filter.end_date)
                        ) 
                    ) &
                    Q(line__name__contains=_filter.line.name)
                )
                
            else:
                propositons = UserProposition.objects.filter(status='в работе')
            try:
                deals = Deal.objects.filter(
                    user_request=user
                )
            except Exception as e:
                deals = None
        else:
            propositons = UserProposition.objects.filter(status='в работе')

        results = []
        domain = request.get_host()
        for proposition in propositons:
            room_id = None
            if request.GET.get('id', None):
                try:
                    room_id = Room.objects.get(
                        Q(request_id=request.GET.get('id', None)) &
                        Q(proposition_id=proposition.pk)
                    ).pk
                except Exception:
                    room_id = None
            try:
                path_image_container = proposition.container.image.url
            except Exception:
                path_image_container = None
            if path_image_container:
                container_image_url = 'http://{domain}{path}'.format(
                    domain=domain, path=path_image_container)
            else:
                container_image_url = None
            try:
                path_image = proposition.user.image.url
            except Exception:
                path_image = None
            if path_image:
                user_image_url = 'http://{domain}{path}'.format(
                    domain=domain, path=path_image)
            else:
                user_image_url = None

            status = False
            if deals:
                _deal = [*[deal.user_proposition.pk for deal in deals], *[deal.user_request.pk for deal in deals]]
                for deal in _deal:
                    if proposition.user.id == deal and user.pk != proposition.user.id:
                        status = True
                        break

            results.append({
                "id":  proposition.id,
                "user": {
                    "id": proposition.user.id,
                    "name": proposition.user.first_name,
                    "lastname": proposition.user.last_name if proposition.user.last_name else None,
                    "onesignal_token": proposition.user.onesignal_token,
                    "image": user_image_url,
                },
                "line": {
                    "id": proposition.line.id,
                    "name": proposition.line.name,
                    
                },
                "city": {
                    "id": proposition.city.id if proposition.city else None,
                    "name": proposition.city.name if proposition.city else None
                },
                "room_id": room_id if room_id else None,
                "amount": proposition.amount,
                "container": {
                    "id": proposition.container.id,
                    "name": proposition.container.name,
                    "image": container_image_url
                },
                "created_at": int(proposition.created_at.timestamp()),
                "is_partner": status,
                "start_date": int(proposition.start_date.timestamp()),
                "end_date": int(proposition.end_date.timestamp())
            })

        return Response(
            results[offset:limit+offset]
        )


class CreateRequestsAPI(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = UserRequest.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = GenericRequestSerializer

    def perform_create(self, serializer):
        user = User.objects.get(
            token=self.request.headers['Authorization'])
        return serializer.save(user=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except AssertionError:
            return Response({"status": "already exists"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        instance = self.perform_create(serializer)
        instance_serializer = GetGenericRequestSerializer(instance)
        return Response(instance_serializer.data)


# class ActionRequestsAPI(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.AllowAny, )
#     queryset = UserRequest.objects.all()
#     parser_classes = (JSONParser, MultiPartParser, FormParser)
#     serializer_class = GenericRequestSerializer

#     def partial_update(self, request, pk, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
class ActionRequestsAPI(generics.RetrieveUpdateAPIView, UpdateModelMixin):
    permission_classes = (permissions.AllowAny, )
    queryset = UserRequest.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = GenericUpdateRequestSerializer


    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class CreatePropositionAPI(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = UserProposition.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = GenericPropositionSerializer

    def perform_create(self, serializer):
        user = User.objects.get(
            token=self.request.headers['Authorization'])
        return serializer.save(user=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except AssertionError:
            return Response({"status": "already exists"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        instance = self.perform_create(serializer)
        instance_serializer = GetGenericPropositionSerializer(instance)
        return Response(instance_serializer.data)


# class ActionPropositionAPI(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.AllowAny, )
#     queryset = UserProposition.objects.all()
#     parser_classes = (JSONParser, MultiPartParser, FormParser)
#     serializer_class = GenericPropositionSerializer

#     def partial_update(self, request, pk, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

class ActionPropositionAPI(generics.RetrieveUpdateAPIView, UpdateModelMixin):
    permission_classes = (permissions.AllowAny, )
    queryset = UserProposition.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = GenericUpdatePropositionSerializer

    def partial_update(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class DeletePropositionAPI(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = UserProposition.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = PropositionSerializer

class DeleteRequestAPI(generics.DestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = UserRequest.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = RequestSerializer
