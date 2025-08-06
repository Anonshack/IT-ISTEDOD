from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import UsefulProgram, OnlineResource, VideoResource
from .serializers import UsefulProgramSerializer, OnlineResourceSerializer, VideoResourceSerializer


# UsefulProgram Views
class UsefulProgramListView(generics.ListAPIView):
    queryset = UsefulProgram.objects.all()
    serializer_class = UsefulProgramSerializer


class UsefulProgramAdminView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = UsefulProgram.objects.all()
    serializer_class = UsefulProgramSerializer
    permission_classes = [IsAdminUser]


# OnlineResource Views
class OnlineResourceListView(generics.ListAPIView):
    queryset = OnlineResource.objects.all()
    serializer_class = OnlineResourceSerializer


class OnlineResourceAdminView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = OnlineResource.objects.all()
    serializer_class = OnlineResourceSerializer
    permission_classes = [IsAdminUser]


# VideoResource Views
class VideoResourceListView(generics.ListAPIView):
    queryset = VideoResource.objects.all()
    serializer_class = VideoResourceSerializer


class VideoResourceAdminView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoResource.objects.all()
    serializer_class = VideoResourceSerializer
    permission_classes = [IsAdminUser]

