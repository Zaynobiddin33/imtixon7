from django.urls import path
from .views import *

urlpatterns = [
    path('staff-create', add_staff),
    path('staff-list', staff_list),
    path('attendence-create/<int:id>', attendence_create),
    path('attendence-day', daily_attendence),
    path('attendence-week', weekly_attendence)


]