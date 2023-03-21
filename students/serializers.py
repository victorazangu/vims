from rest_framework import serializers

from students.models import  Student


class StudentSerializer(serializers.Serializer):
    class Meta:
        model = Student
        field = '__all__'