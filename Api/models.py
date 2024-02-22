from django.db import models

# Create your models here.

class Staff(models.Model):
    f_name = models.CharField(max_length = 200)
    l_name = models.CharField(max_length = 200)
    job = models.CharField(max_length = 200)

class Staff_attendence(models.Model):
    staff = models.ForeignKey(Staff, on_delete = models.CASCADE)
    arrived_time = models.DateTimeField(auto_now_add  = True)
