from django.db import models
from header.models import Employee

# Create your models here.


class Assigwork(models.Model):
    work_name = models.CharField(max_length = 200)  
    members = models.ForeignKey(Employee,on_delete=models.CASCADE)