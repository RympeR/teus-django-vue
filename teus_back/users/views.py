from django.http import request
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, AdminSerializer
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import permission_classes, renderer_classes
from containers.raw_sql import UserFilter
from .models import User, Admin
from rest_framework import status

@renderer_classes((JSONRenderer,))
@permission_classes((permissions.AllowAny,))
class UserAPI(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser, )

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
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    parser_classes = (MultiPartParser, FormParser, JSONParser, )
    userfilter = UserFilter()
    
    def post(self, *args, **kwargs):
        try:
            admin = Admin.objects.filter(
                login=self.request.data['email'],
                password=self.request.data['password']
            )[0]
        except Exception as e:
            print(e)
            admin = None
        print(admin)
        print(self.request.data)
        if admin:
            return Response(
                {
                    "status": True,
                    "id": admin.id,
                    "login": admin.login,
                    "password": admin.password,
                    "token": admin.token
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "status": False
                }
            )

    def get(self, *args, **kwargs):
        data =  dict(self.request.data)
        data['token'] =Admin.generate_token(data['email'][0])
        admin = AdminSerializer(data=data)
        if admin.is_valid():
            return Response(
                {
                    "status": True,
                    "token": admin.data['token']
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "status": False,
                    "data": admin.data
                }
            )

    def put(self, *args, **kwargs):
        print('maded')
        try:
            admin = Admin.objects.get(token=self.request.headers['Authorization'])
        except Exception:
            admin = None
        if admin:
            admin = AdminSerializer(
                instance=admin, data=self.request.data)
            if admin.is_valid():
                admin.save()
                response = Response({
                    "id": admin.data['id']
                }, status=status.HTTP_200_OK)
                response["Access-Control-Allow-Origin"] = 'Authorization'
                return response
            else:
                return Response(
                    admin.data
                )
        else:
            return Response(
                {
                    "status": "invalid token"
                }
            )