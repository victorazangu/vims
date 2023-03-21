from django.db import models

from users.models import CustomUser
# Create your models here.

class Blog(models.Model):
    # blog_id = models.IntegerField( primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    author =models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.TextField(max_length=5000)
    #image =models.ImageField()
    def __str__(self) -> str:
        return self.title