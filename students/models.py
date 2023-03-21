from django.db import models

from courses.models import Course
from programs.models import Program

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField(
        primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    phone = models.CharField(max_length=255,unique=True)
    # profile = models.ImageField()
    program =models.ForeignKey(Program,on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    adm_no = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    status =  models.BooleanField(default=True)