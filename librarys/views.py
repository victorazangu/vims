
from .serializers import LibrarySerializer
from .models import Library
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# cart views


class LibraryList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    filterset_fields = ['title',
                        'author_name',
                        'category',]
    search_fields = ['title',
                     'author_name',
                     'category',]
    ordering_fields = ['title',
                       'author_name',
                       'category',]


class SingleLibraryView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    filterset_fields = ['title',
                        'author_name',
                        'category',]
    search_fields = ['title',
                     'author_name',
                     'category',]
    ordering_fields = ['title',
                       'author_name',
                       'category',]
