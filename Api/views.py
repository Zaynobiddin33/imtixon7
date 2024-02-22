from django.shortcuts import render

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from . import serializers
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import update_session_auth_hash
from rest_framework.authtoken.models import Token
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework.authentication import *
from rest_framework.permissions import IsAuthenticated
from . import models
from datetime import datetime, date
from datetime import datetime, timedelta
    
# Create your views here.

@api_view(['POST'])
def add_staff(request):
    f_name = request.data['f_name']
    l_name = request.data['l_name']
    position = request.data['job']
    data = models.Staff.objects.create(
        f_name = f_name,
        l_name = l_name,
        job = position
    )
    serializer = serializers.StaffSerializer(data)
    context = {
        'detail': "staff's created succesfully",
        'staff' : serializer.data
    }
    return Response(context)

    
@api_view(['GET'])
def staff_list(request):
    workers = models.Staff.objects.all()
    serializer = serializers.StaffSerializer(workers, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def attendence_create(request, id):
    worker = models.Staff.objects.get(id = id)
    attendence = models.Staff_attendence.objects.create(
        staff = worker
    )
    serializer = serializers.Staff_attendenceSerializer(attendence)
    return Response(
        serializer.data
    )

@api_view(['GET'])
def daily_attendence(request):
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    filtered =models.Staff_attendence.objects.filter(arrived_time__year = year, arrived_time__month = month,  arrived_time__day = day)
    serializer = serializers.Staff_attendenceSerializer(filtered, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def weekly_attendence(request):
    now = datetime.now()
    week_before = now - timedelta(days = 7)
    filtered = models.Staff_attendence.objects.filter(arrived_time__gte = week_before, arrived_time__lte = now)
    serializer = serializers.Staff_attendenceSerializer(filtered, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def monthly_attendence(request):
    now = datetime.now()
    month_before = str(now)
    print(new)
    filtered = models.Staff_attendence.objects.filter(arrived_time__gte = month_before, arrived_time__lte = now)
    print(month_before)
    return Response({})