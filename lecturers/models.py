from django.db import models

from courses.models import Course

# Create your models here.


class Lecturer(models.Model):
    lecturer_id = models.IntegerField(
        primary_key=True, editable=False, unique=True)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    id_no = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    # profile =models.ImageField()
    status = models.BooleanField()
    course_1 = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, related_name="course_1")
    course_2 = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, related_name="course_2")
    course_3 = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, related_name="course_3")
    course_4 = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, related_name="course_4")
    course_5 = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, related_name="course_5")
