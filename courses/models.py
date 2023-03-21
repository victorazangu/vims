from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.IntegerField( primary_key=True, editable=False, unique=True)
    course_name  = models.CharField(max_length=255)
    description = models.CharField(max_length=450)
    category=models.CharField(max_length=255)
    #coursea_image = models.ImageField()
    duration =models.CharField(max_length=255)
    status =models.BooleanField()
    type =models.CharField(max_length=255)
    amount =models.DecimalField(max_digits=6,decimal_places=2)