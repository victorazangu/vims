from rest_framework import serializers

from student_payments.models import  StudentPayment


class StudentPaymentSerializer(serializers.Serializer):
    class Meta:
        model = StudentPayment
        field = '__all__'