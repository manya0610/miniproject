# Buildings/urls.py
from django.urls import path
from .views import (
BuildingListView,
BuildingDetailView, # new
BuildingCreateView,
BuildingDeleteView, # new
BuildingUpdateView, # new
ApartmentDeleteView,
)
urlpatterns = [
path('<int:pk>/edit/',
BuildingUpdateView.as_view(), name='building_edit'), # new
path('<int:pk>/',
BuildingDetailView.as_view(), name='building_detail'), # new
path('<int:pk>/delete/',
BuildingDeleteView.as_view(), name='building_delete'), # new
path('', BuildingListView.as_view(), name='building_list'),
path('new/',
BuildingCreateView.as_view(), name='building_new'),
path('<int:building_pk>/apartment/<int:pk>/delete', ApartmentDeleteView.as_view(), name='apartment_delete'),

]