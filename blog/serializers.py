from rest_framework import serializers

from blog.models import Blog


class BlogSerializer(serializers.Serializer):
    class Meta:
        model = Blog
        field = '__all__'
