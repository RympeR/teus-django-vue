from django.urls import path

from .views import *

urlpatterns = [
    path('get-request/<int:request_id>/', RequestAPI.as_view() ,name='RequestProfile'),
    path('get-requests-list', RequestsList.as_view() ,name='RequestFullList'),
    path('create-request/', RequestAPI.as_view() ,name='RequestCreate'),
    path('update-request/<int:request_id>/', RequestAPI.as_view() ,name='RequestUpdate'),
    path('delete-request/<int:request_id>/', RequestAPI.as_view() ,name='RequestDelete'),

    path('get-proposition/<int:proposition_id>/', PropositionAPI.as_view() ,name='PropositionProfile'),
    path('get-proposition-list', PropositionList.as_view() ,name='PropositionFullList'),
    path('create-proposition/', PropositionAPI.as_view() ,name='PropositionCreate'),
    path('update-proposition/<int:proposition_id>/', PropositionAPI.as_view() ,name='PropositionUpdate'),
    path('delete-proposition/<int:proposition_id>/', PropositionAPI.as_view() ,name='PropositionDelete'),

]