from django.urls import path, include
from .views import *

urlpatterns = [
    path('profile/<int:user_id>/', UserAPI.as_view(), name='UserProfile'),
    
    path('profile/', UserListAPI.as_view(), name='UserFullList'),
    path('create-profile/', UserAPI.as_view(), name='UserCreate'),
    path('update-profile/<int:user_id>/', UserAPI.as_view(), name='UserUpdate'),
    path('delete-profile/<int:user_id>/', UserAPI.as_view(), name='UserDelete'),
    path('get-users-list', UsersList.as_view() ,name='UsersFilterList'),
    
    path('login/', UserTokenAPI.as_view(), name='UserCreate'),
    path('api-profile-update/', UserTokenAPI.as_view(), name='UserUpdate'),
    path('api-profile-delete/', UserTokenAPI.as_view(), name='UserDelete'),
    path('api-profile-get/', UserTokenAPI.as_view(), name='UserProfile'),
    
    
    
    # path('create-admin/', AdminAPI.as_view(), name='UserCreate'),
    path('admin/profile/', AdminAPI.as_view(), name='UserProfile'),
    path('admin/', AdminAPI.as_view(), name='UserProfile'),
    path('change-password/', ChangePasswordAPI.as_view(), name='UserUpdate'),
]
