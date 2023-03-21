from django.db import models

# Create your models here.


class Library(models.Model):
    book_id = models.IntegerField(
        primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    # image =models.ImageField()

    def __str__(self) -> str:
        return self.title + "(" + self.category+")"
