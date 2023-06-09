from django.conf import settings
from django.db import models
from courses.models import Course


# Create your models here.
class SubscribedCourse(models.Model):
    subscribed_course_id = models.IntegerField(
        primary_key=True, editable=False, unique=True)
    course =models.ForeignKey(Course,on_delete=models.CASCADE)
    student =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    subscribed_date =models.DateTimeField()
    
        
    def __str__(self) -> str:
        return self.course.course_name