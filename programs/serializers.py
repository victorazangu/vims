from rest_framework import serializers

from programs.models import  Program


class ProgramSerializer(serializers.Serializer):
    class Meta:
        model = Program
        field = '__all__'