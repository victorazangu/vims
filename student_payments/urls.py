from django.urls import path
from . import views

urlpatterns = [
    path('students-payment', views.StudentPaymentList.as_view()),
    path('students-payment/<int:pk>', views.SingleStudentPaymentView.as_view()),
]
