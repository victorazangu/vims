from django.urls import path
from . import views

urlpatterns = [
    path('programs', views.ProgramList.as_view()),
    path('program/<int:pk>', views.SingleProgramView.as_view()),
]
