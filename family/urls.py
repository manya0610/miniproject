# articles/urls.py
from django.urls import path
from .views import (
FamilyMemberListView,
FamilyMemberUpdateView, # new
FamilyMemberDetailView, # new
FamilyMemberDeleteView, # new
FamilyMemberCreateView,
)
urlpatterns = [
path('<int:pk>/edit/',
FamilyMemberUpdateView.as_view(), name='familymember_edit'), # new
path('<int:pk>/',
FamilyMemberDetailView.as_view(), name='familymember_detail'), # new
path('<int:pk>/delete/',
FamilyMemberDeleteView.as_view(), name='familymember_delete'), # new
path('', FamilyMemberListView.as_view(), name='familymember_list'),
path('new/',
FamilyMemberCreateView.as_view(), name='familymember_new'),

]