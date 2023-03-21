from django.db import models
from courses.models import Course

from students.models import Student

# Create your models here.
class SubscribedCourse(models.Model):
    subscribed_course_id = models.IntegerField(
        primary_key=True, editable=False, unique=True)
    course =models.ForeignKey(Course,on_delete=models.CASCADE)
    student =models.ForeignKey(Student,on_delete=models.CASCADE)
    subscribed_date =models.DateTimeField()