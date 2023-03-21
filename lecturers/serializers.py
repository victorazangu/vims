from rest_framework import serializers

from lecturers.models import  Lecturer


class LecturerSerializer(serializers.Serializer):
    class Meta:
        model = Lecturer
        field = '__all__'