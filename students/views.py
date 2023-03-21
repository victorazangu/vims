
from .serializers import StudentSerializer
from .models import Student
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# cart views


class StudentList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ['name',
                        'email'
                        ]
    search_fields = ['name',
                     'email'
                     ]
    ordering_fields = ['name',]


class SingleStudentView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ['name',
                        'email'
                        ]
    search_fields = ['name',
                     'email'
                     ]
    ordering_fields = ['name',]
