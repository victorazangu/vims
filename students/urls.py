from django.urls import path
from . import views

urlpatterns = [
    path('students', views.StudentList.as_view()),
    path('student/<int:pk>', views.SingleStudentView.as_view()),
]
