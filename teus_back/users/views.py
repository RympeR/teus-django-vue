from django.http import request
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import permission_classes, renderer_classes, api_view, parser_classes
from containers.raw_sql import UserFilter
from .models import User
from rest_framework import status
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return
@renderer_classes((JSONRenderer,))
@permission_classes((permissions.AllowAny,))
class UserAPI(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser, )
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, *args, **kwargs):
        try:
            print(self.request.headers)
            user = User.objects.get(token=self.request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            user = UserSerializer.getProfile(**kwargs)
            domain = self.request.get_host()
            try:
                path_image = user.image.url
                image_url = 'http://{domain}{path}'.format(
                    domain=domain, path=path_image)
            except ValueError:
                image_url = ''
            return Response(
                {
                    "user_id": user.id,
                    "phone": user.phone,
                    "image": image_url,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "company": user.company
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )
    def post(self, *args, **kwargs):
        data = dict(self.request.data)  
        print(type(data['phone'][0]))
        data['token'] = User.generate_token(data['phone'][0])
        print(data['token'])
        user_token = UserSerializer.create(data)
        return Response(
            {
                "status": "ok",
                "token": user_token
            }, status=status.HTTP_200_OK
        )


    def put(self, *args, **kwargs):
        try:
            user = User.objects.get(token=self.request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            data = dict(self.request.data)
            data['user_id'] = kwargs['user_id']
            user = UserSerializer.update(data)
            domain = self.request.get_host()
            try:
                path_image = user.image.url
                image_url = 'http://{domain}{path}'.format(
                    domain=domain, path=path_image)
            except ValueError:
                image_url = ''
            return Response(
                {
                    "user_id": user.id,
                    "image": image_url,
                    "phone": user.phone,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "company": user.company
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )

    def delete(self, *args, **kwargs):
        try:
            user = User.objects.get(token=self.request.headers['Authorization'])
        except Exception:
            user = None
        if user:
            user = UserSerializer.deleteUser(
                **kwargs
            )
            return Response(
                {
                    "user_id": user[0]
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )

@permission_classes((permissions.AllowAny,))
@renderer_classes((JSONRenderer,))
class UserListAPI(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    parser_classes = (MultiPartParser, FormParser, JSONParser, )
    def get(self, *args, **kwargs):


        users = UserSerializer.getList()
        users_list = users.values()
        domain = self.request.get_host()
        for ind, user in enumerate(users_list):
            try:
                path_image = users[ind].image.url
                image_url = 'http://{domain}{path}'.format(
                    domain=domain, path=path_image)
            except ValueError:
                image_url = ''
            users_list[ind]['image'] = image_url
        print(users_list)
        return Response(
            {
                "results": users_list,
                "status": "ok"
            }, status=status.HTTP_200_OK
        )
class UsersList(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    parser_classes = (MultiPartParser, FormParser, JSONParser, )
    userfilter = UserFilter()
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get(self, request):

        data = self.userfilter.get_users(request, 'postgres', '1111')
        result = {
            "results": []
        }
        for ind, row in enumerate(data):
            domain = self.request.get_host()
            print(f'\t\t{row[5]}')
            path_image = f'/media/{row[5]}'
            image_url = 'http://{domain}{path}'.format(
                domain=domain, path=path_image)
            print(image_url)
            result['results'].append({
                "id": row[0],
                "phone": row[1],
                "last_name": row[3],
                "first_name": row[2],
                "image": image_url,
            })
        response = Response(
            {
                "results": result['results']
            }, status=status.HTTP_200_OK
        )
        response["Access-Control-Allow-Origin"] = 'Authorization'
        return response



class AdminAPI(APIView):
    permission_classes= permissions.AllowAny,
    parser_classes= (MultiPartParser, FormParser, JSONParser,)
    renderer_classes= JSONRenderer,
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, request):
        try:
            user = User.objects.filter(
                first_name=request.data['email'],
                password=request.data['password'],
                is_admin=True,
            )[0]
        except Exception as e:
            
            user = None
        print(user)
        if user:
            return Response(
                {
                    "token": user.token
                }
            )
        else:
            return Response(
                {
                    "status": "failure"
                }, status=status.HTTP_404_NOT_FOUND
            )



    def get(self, request):
        try :
            print(request.headers)
            user = User.objects.get(
                Q(token=request.headers['Authorization']) 
            )
        except Exception as e:
            print(e)
            user = None
        if user:
            print(f'\n\ngot {user}\n\n') 
            return Response(
                {
                    "status": True,
                    "user_id": user.id,
                    "login": user.first_name,
                    "password": user.password
                }
            )
        else:
            print(request.headers['Authorization'])
            print(user)
            return Response(
                {
                    "status": False
                }, status=status.HTTP_423_LOCKED
            )

class ChangePasswordAPI(APIView):
    permission_classes= permissions.AllowAny,
    parser_classes= (MultiPartParser, FormParser, JSONParser,)
    renderer_classes= JSONRenderer,
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, *args, **kwargs):
        try:
            user = User.objects.get(token=self.request.headers['Authorization'])
        except Exception as e:
            print(e)
            user = None
        print(User)
        if user:
            print( self.request.data)
            user = UserSerializer.update_password(user, self.request.data['new_password'])
            print(f"{user} updated")
            response = Response(
                {
                     "user_id": user.id,
                    "login": user.first_name,
                    "password": user.password
                }
            )
            print(f"\n\n\t{response}\n\n")
            return response
        else:
            return Response(
                {
                    "status": "failure"
                }
            )
