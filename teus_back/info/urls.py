from django.urls import path

from .views import *

urlpatterns = [
    # path('get-workout-filtered-list/', WorkoutFilteredList.as_view() ,name='WorkoutFilteredList'),
    path('get-container/<int:container_id>/', ContainerAPI.as_view() ,name='ContainerProfile'),
    path('get-containers-list/', get_containers_list ,name='ContainerFullList'),
    path('create-container/', ContainerAPI.as_view() ,name='ContainerCreate'),
    path('update-container/<int:container_id>/', ContainerAPI.as_view() ,name='ContainerUpdate'),
    path('delete-container/<int:container_id>/', ContainerAPI.as_view() ,name='ContainerDelete'),

    path('get-city/<int:city_id>/', CityAPI.as_view() ,name='CityProfile'),
    path('get-cities-list/', get_cities_list ,name='CityFullList'),
    path('create-city/', CityAPI.as_view() ,name='CityCreate'),
    path('update-city/<int:city_id>/', CityAPI.as_view() ,name='CityUpdate'),
    path('delete-city/<int:city_id>/', CityAPI.as_view() ,name='CityDelete'),

    path('get-line/<int:line_id>/', LineAPI.as_view() ,name='LineProfile'),
    path('get-lines-list/', get_lines_list ,name='LineFullList'),
    path('create-line/', LineAPI.as_view() ,name='LineCreate'),
    path('update-line/<int:line_id>/', LineAPI.as_view() ,name='LineUpdate'),
    path('delete-line/<int:line_id>/', LineAPI.as_view() ,name='LineDelete'),

]