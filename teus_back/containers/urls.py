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
    path('proposition-list/', FilteredPropositions.as_view() ,name='PropositionFilteredList'),
    path('create-proposition/', PropositionAPI.as_view() ,name='PropositionCreate'),
    path('update-proposition/<int:proposition_id>/', PropositionAPI.as_view() ,name='PropositionUpdate'),
    path('delete-proposition/<int:proposition_id>/', PropositionAPI.as_view() ,name='PropositionDelete'),


    path('get-deal/<int:deal_id>/', DealAPI.as_view() ,name='DealProfile'),
    path('get-deal-list', DealsList.as_view() ,name='DealFullList'),
    path('create-deal/', DealAPI.as_view() ,name='DealCreate'),
    path('update-deal/<int:deal_id>/', DealAPI.as_view() ,name='DealUpdate'),
    path('delete-deal/<int:deal_id>/', DealAPI.as_view() ,name='DealDelete'),

]