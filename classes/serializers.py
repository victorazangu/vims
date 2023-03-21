from rest_framework import serializers

from classes.models import Class


class ClassSerializer(serializers.Serializer):
    class Meta:
        model = Class
        field = '__all__'
