from django.conf import settings
from django.db import models



# Create your models here.


class StudentPayment(models.Model):
    student_payment_id = models.IntegerField(
        primary_key=True, editable=False, unique=True)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    purpose = models.CharField(max_length=450)
    paid_via = models.CharField(max_length=255)
    reference_no = models.CharField(max_length=255)
    paid_on = models.DateField()
    paid_by = models.CharField(max_length=450)
    
    def __str__(self) -> str:
        return self.student.name + "(" + self.purpose+")"
