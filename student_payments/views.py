
from .serializers import StudentPaymentSerializer
from .models import StudentPayment
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# cart views


class StudentPaymentList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StudentPayment.objects.all()
    serializer_class = StudentPaymentSerializer
    filterset_fields = ['student',
                        'purpose',
                        ]
    search_fields = ['student', 'purpose']
    ordering_fields = ['student',]


class SingleStudentPaymentView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StudentPayment.objects.all()
    serializer_class = StudentPaymentSerializer
    filterset_fields = ['student',
                        'purpose',
                        ]
    search_fields = ['student', 'purpose']
    ordering_fields = ['student',]
