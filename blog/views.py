
from .serializers import BlogSerializer
from .models import Blog
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated


# cart views


class BlogList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filterset_fields = ['title']
    search_fields = ['title', 'description', 'content']
    ordering_fields = ['title']


class SingleBlogView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filterset_fields = ['title']
    search_fields = ['title', 'description', 'content']
    ordering_fields = ['title']
