from django.urls import path

from .views import *

urlpatterns = [
    # path('get-workout-filtered-list/', WorkoutFilteredList.as_view() ,name='WorkoutFilteredList'),
    path('get-container/<int:pk>/', ContainerAPI.as_view() ,name='ContainerProfile'),
    path('get-containers-list/', get_containers_list ,name='ContainerFullList'),
    path('get-containers-list-api/', get_containers_list_api ,name='ContainerFullList'),
    path('create-container/', CreateContainerAPI.as_view() ,name='ContainerCreate'),
    path('update-container/<int:pk>/', ContainerAPI.as_view() ,name='ContainerUpdate'),
    path('delete-container/<int:pk>/', ContainerAPI.as_view() ,name='ContainerDelete'),

    path('get-city/<int:pk>/', CityAPI.as_view() ,name='CityProfile'),
    path('get-cities-list/', get_cities_list ,name='CityFullList'),
    path('get-cities-list-api/', get_cities_list_api ,name='CityFullList'),
    path('create-city/', CityAPI.as_view() ,name='CityCreate'),
    path('update-city/<int:pk>/', CityAPI.as_view() ,name='CityUpdate'),
    path('delete-city/<int:pk>/', CityAPI.as_view() ,name='CityDelete'),

    path('get-line/<int:pk>/', LineAPI.as_view() ,name='LineProfile'),
    path('get-lines-list-api/', get_lines_list_api ,name='LineFullList'),
    path('get-lines-list/', get_lines_list ,name='LineFullList'),
    path('create-line/', CreateLineAPI.as_view() ,name='LineCreate'),
    path('update-line/<int:pk>/', LineAPI.as_view() ,name='LineUpdate'),
    path('delete-line/<int:pk>/', LineAPI.as_view() ,name='LineDelete'),

]
