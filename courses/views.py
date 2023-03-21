
from .serializers import CourseSerializer
from .models import Course
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# cart views


class CourseList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_fields = ['course_name']
    search_fields = ['course_name', 'description', 'category']
    ordering_fields = ['course_name']


class SingleCourseView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_fields = ['course_name']
    search_fields = ['course_name', 'description', 'category']
    ordering_fields = ['course_name']
