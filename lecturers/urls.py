from django.urls import path
from . import views

urlpatterns = [
    path('lecturers', views.LecturerList.as_view()),
    path('lecturer/<int:pk>', views.SingleLecturerView.as_view()),
]
