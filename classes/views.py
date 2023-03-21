
from .serializers import ClassSerializer
from .models import Class
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# cart views


class ClassList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    filterset_fields = ['course', 'program', 'lecturer']
    search_fields = ['course', 'program', 'lecturer']
    ordering_fields = ['course', 'program', 'lecturer']


class SingleClassView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    filterset_fields = ['course', 'program', 'lecturer']
    search_fields = ['course', 'program', 'lecturer']
    ordering_fields = ['course', 'program', 'lecturer']
