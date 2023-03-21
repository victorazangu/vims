from django.urls import path
from . import views

urlpatterns = [
    path('classes', views.ClassList.as_view()),
    path('classes/<int:pk>', views.SingleClassView.as_view()),
]
