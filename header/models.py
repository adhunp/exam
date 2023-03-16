from django.db import models
from email.policy import default

# Create your models here.
class Hlogin(models.Model):
    username = models.CharField(max_length = 20) 
    password = models.CharField(max_length = 20)

class Employee(models.Model):
    e_name = models.CharField(max_length = 20)  #charfiled is mean varchar(20)
    e_email = models.CharField(max_length = 20)
    e_qualification = models.CharField(max_length = 20)
    e_experience = models.BigIntegerField()
    e_gender = models.CharField(max_length = 20)
    e_dob = models.CharField(max_length = 20)
    e_password = models.CharField(max_length = 20)
    e_phone = models.BigIntegerField()

class Addleader(models.Model):
    team_name = models.CharField(max_length = 20)  
    leader = models.ForeignKey(Employee,on_delete=models.CASCADE)


class Addproject(models.Model):
    p_name = models.CharField(max_length = 20)  
    leadername = models.ForeignKey(Addleader,on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)

class Not(models.Model):
    hr = models.ForeignKey(Addleader,on_delete=models.CASCADE)
