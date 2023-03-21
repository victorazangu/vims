from rest_framework import serializers

from courses.models import  Course


class CourseSerializer(serializers.Serializer):
    class Meta:
        model = Course
        field = '__all__'