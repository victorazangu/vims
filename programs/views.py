
from .serializers import ProgramSerializer
from .models import Program
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# cart views


class ProgramList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    filterset_fields = ['program_name',
                        'contact_person',
                        'venue',]
    search_fields = ['program_name',]
    ordering_fields = ['program_name',]


class SingleProgramView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    filterset_fields = ['program_name',
                        'contact_person',
                        'venue',]
    search_fields = ['program_name',]
    ordering_fields = ['program_name',]
