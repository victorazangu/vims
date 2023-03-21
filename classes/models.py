from django.conf import settings
from django.db import models
from courses.models import Course
from programs.models import Program
from django.contrib.auth.models import User


lecturer = settings.AUTH_USER_MODEL
# Create your models here.
class Class(models.Model):
    # class_id = models.IntegerField( primary_key=True, editable=False, unique=True)
    course = models.ForeignKey(Course,on_delete=models.PROTECT)
    program = models.ForeignKey(Program,on_delete=models.PROTECT)
    lecturer = models.ForeignKey(lecturer,on_delete=models.PROTECT)
    location = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    start_day = models.CharField(max_length=255)
    end_day = models.CharField(max_length=255)
    starts = models.DateField()
    ends = models.DateField()
    type = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.course.course_name + self.lecturer.first_name
