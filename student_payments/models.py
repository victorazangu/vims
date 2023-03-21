from django.db import models

from students.models import Student

# Create your models here.


class StudentPayment(models.Model):
    student_payment_id = models.IntegerField(
        primary_key=True, editable=False, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    purpose = models.CharField(max_length=450)
    paid_via = models.CharField(max_length=255)
    reference_no = models.CharField(max_length=255)
    paid_on = models.DateField()
    paid_by = models.CharField(max_length=450)
