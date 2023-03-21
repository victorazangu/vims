from rest_framework import serializers

from librarys.models import  Library


class LibrarySerializer(serializers.Serializer):
    class Meta:
        model = Library
        field = '__all__'