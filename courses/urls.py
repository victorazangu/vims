from django.urls import path
from . import views

urlpatterns = [
    path('courses', views.CourseList.as_view()),
    path('course/<int:pk>', views.SingleCourseView.as_view()),
]
