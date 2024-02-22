from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Staff)
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display =('f_name','l_name')
    
admin.site.register(Staff_attendence)