from django.db import models

# Create your models here.


class Program(models.Model):
    program_id = models.IntegerField(
        primary_key=True, editable=False, unique=True)
    program_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    starts = models.DateField()
    ends = models.DateField()
    status = models.BooleanField()
