from django.urls import path

from .views import *

urlpatterns = [
    path('get-request/<int:request_id>/', RequestAPI.as_view() ,name='RequestProfile'),
    path('create-request/', RequestAPI.as_view() ,name='RequestCreate'),
    path('get-requests-list', RequestsList.as_view() ,name='RequestFullList'),
    path('get-requests-api-list', RequestsAPIList.as_view() ,name='RequestFullList'),
    path('update-request/<int:request_id>/', RequestAPI.as_view() ,name='RequestUpdate'),
    path('delete-request/<int:request_id>/', DeleteRequestAPI.as_view() ,name='RequestDelete'),

    path('get-proposition/<int:proposition_id>/', PropositionAPI.as_view() ,name='PropositionProfile'),
    path('create-proposition/', PropositionAPI.as_view() ,name='PropositionCreate'),
    path('get-proposition-list', PropositionList.as_view() ,name='PropositionFullList'),
    path('get-proposition-api-list', PropositionAPIList.as_view() ,name='PropositionFullList'),
    path('proposition-list/', FilteredPropositions.as_view() ,name='PropositionFilteredList'),
    path('update-proposition/<int:proposition_id>/', PropositionAPI.as_view() ,name='PropositionUpdate'),
    path('delete-proposition/<int:proposition_id>/', DeletePropositionAPI.as_view() ,name='PropositionDelete'),


    path('get-deal-list', DealsList.as_view() ,name='DealFullList'),
    path('get-deal-api-list', DealsAPIList.as_view() ,name='DealFullList'),
    path('get-deal/<int:deal_id>/', DealAPI.as_view() ,name='DealProfile'),
    path('create-deal/', DealAPI.as_view() ,name='DealCreate'),
    path('update-deal/<int:deal_id>/', DealAPI.as_view() ,name='DealUpdate'),
    path('delete-deal/<int:deal_id>/', DealAPI.as_view() ,name='DealDelete'),
    path('quit-out-of-chat/<int:pk>', GetOutOfChat.as_view()),
    path('get-apidoc-api-proposition/', APDICOUserPropositionsAPI.as_view() ,name='PropositionProfile'),
    
    path('get-api-proposition/', UserPropositionsAPI.as_view() ,name='PropositionProfile'),
    path('create-api-proposition/', CreatePropositionAPI.as_view() ,name='PropositionCreate'),
    path('update-api-proposition/<int:pk>', ActionPropositionAPI.as_view() ,name='PropositionCreate'),
    
    path('get-apidoc-api-request/', APIDOCUserRequests.as_view() ,name='RequestAPIProfile'),
    
    path('get-api-request/', UserRequestsAPI.as_view() ,name='RequestAPIProfile'),
    path('create-api-request/', CreateRequestsAPI.as_view() ,name='RequestAPICreate'),
    path('update-api-request/<int:pk>', ActionRequestsAPI.as_view() ,name='RequestAPICreate'),
    
    path('mark-request-status/',UserRequestsAPI.as_view() ,name='RequestAPImark' ),
    path('mark-proposition-status/',UserPropositionsAPI.as_view() ,name='RequestAPImark' ),
]
