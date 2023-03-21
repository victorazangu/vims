from django.urls import path
from . import views

urlpatterns = [
    path('subsribed-courses', views.SubscribedCourseList.as_view()),
    path('subscribed-course/<int:pk>', views.SingleSubscribedCourseView.as_view()),
]
