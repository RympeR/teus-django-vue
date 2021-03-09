from django.urls import path, include
from .views import *

urlpatterns = [
    path('create-profile/', UserAPI.as_view(), name='UserCreate'),
    path('profile/', UserListAPI.as_view(), name='UserFullList'),
    path('profile/<int:user_id>/', UserAPI.as_view(), name='UserProfile'),
    path('update-profile/<int:user_id>/', UserAPI.as_view(), name='UserUpdate'),
    path('delete-profile/<int:user_id>/', UserAPI.as_view(), name='UserDelete'),
    path('get-users-list', UsersList.as_view() ,name='UsersFilterList'),
    
    path('create-admin/', AdminAPI.as_view(), name='UserCreate'),
    path('admin/', AdminAPI.as_view(), name='UserProfile'),
    path('change-password/', AdminAPI.as_view(), name='UserUpdate'),
]
