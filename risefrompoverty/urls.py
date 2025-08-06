from django.urls import path
from .views import (
    UsefulProgramListView, UsefulProgramAdminView,
    OnlineResourceListView, OnlineResourceAdminView,
    VideoResourceListView, VideoResourceAdminView
)

urlpatterns = [
    # UsefulProgram URLs
    path('useful-programs/', UsefulProgramListView.as_view(), name='useful-program-list'),
    path('useful-programs/<int:pk>/', UsefulProgramAdminView.as_view(), name='useful-program-detail'),

    # OnlineResource URLs
    path('online-resources/', OnlineResourceListView.as_view(), name='online-resource-list'),
    path('online-resources/<int:pk>/', OnlineResourceAdminView.as_view(), name='online-resource-detail'),

    # VideoResource URLs
    path('video-resources/', VideoResourceListView.as_view(), name='video-resource-list'),
    path('video-resources/<int:pk>/', VideoResourceAdminView.as_view(), name='video-resource-detail'),
]
