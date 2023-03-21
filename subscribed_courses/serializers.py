from rest_framework import serializers

from subscribed_courses.models import SubscribedCourse


class SubscribedCourseSerializer(serializers.Serializer):
    class Meta:
        model = SubscribedCourse
        field = '__all__'
