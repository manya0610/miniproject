# Notices/urls.py
from django.urls import path
from .views import (
NoticeListView,
NoticeUpdateView, # new
NoticeDetailView, # new
NoticeDeleteView, # new
NoticeCreateView,
CommentDeleteView
)
urlpatterns = [
path('<int:pk>/edit/',
NoticeUpdateView.as_view(), name='notice_edit'), # new
path('<int:pk>/',
NoticeDetailView.as_view(), name='notice_detail'), # new
path('<int:pk>/delete/',
NoticeDeleteView.as_view(), name='notice_delete'), # new
path('', NoticeListView.as_view(), name='notice_list'),
path('new/',
NoticeCreateView.as_view(), name='notice_new'),
 path('<int:notice_pk>/comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment_delete'),


]