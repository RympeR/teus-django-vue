from django.http import request
from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import permission_classes, renderer_classes
from containers.raw_sql import UserFilter

@renderer_classes((JSONRenderer,))
@permission_classes((permissions.AllowAny,))
class UserAPI(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser, )

    def get(self, *args, **kwargs):
        print(*kwargs.keys())
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
            }
        )

    def post(self, *args, **kwargs):

        print(self.request.data)
        user_id = UserSerializer.create(self.request.data)
        return Response(
            {
                "user_id": user_id
            }
        )

    def put(self, *args, **kwargs):
        print(self.request.data)
        data = dict(self.request.data)
        print(data)
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
            }
        )

    def delete(self, *args, **kwargs):
        user = UserSerializer.deleteUser(
            **kwargs
        )
        return Response(
            {
                "user_id": user[0]
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
                "results": users_list
            }
        )

class UsersList(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny, )
    parser_classes = (MultiPartParser, FormParser, JSONParser, )
    userfilter = UserFilter()

    def get(self, request):
        print(request.GET)
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
        return Response(
            {
                "results": result['results']
            }
        )