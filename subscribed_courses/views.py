
from .serializers import SubscribedCourseSerializer
from .models import SubscribedCourse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# cart views


class SubscribedCourseList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SubscribedCourse.objects.all()
    serializer_class = SubscribedCourseSerializer
    filterset_fields = ['course',
                        ]
    search_fields = ['course',
                     ]
    ordering_fields = ['course',]


class SingleSubscribedCourseView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SubscribedCourse.objects.all()
    serializer_class = SubscribedCourseSerializer
    filterset_fields = ['course',
                        ]
    search_fields = ['course',
                     ]
    ordering_fields = ['course',]
