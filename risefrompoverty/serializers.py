from rest_framework import serializers
from .models import UsefulProgram, OnlineResource, VideoResource


class UsefulProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulProgram
        fields = '__all__'


class OnlineResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineResource
        fields = '__all__'


class VideoResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoResource
        fields = '__all__'
