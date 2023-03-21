
from .serializers import LecturerSerializer
from .models import Lecturer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# cart views


class LecturerList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    filterset_fields = ['first_name','second_name']
    search_fields = ['first_name','second_name']
    ordering_fields = ['first_name','second_name']


class SingleLecturerView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    filterset_fields = ['first_name','second_name']
    search_fields = ['first_name','second_name']
    ordering_fields = ['first_name','second_name']
