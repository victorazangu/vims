from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    # blog_id = models.IntegerField( primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    author =models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=5000)
    #image =models.ImageField()
    def __str__(self) -> str:
        return self.title