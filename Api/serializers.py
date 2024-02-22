from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import *


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class Staff_attendenceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Staff_attendence
        fields = '__all__'