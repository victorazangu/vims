from django.urls import path
from . import views

urlpatterns = [
    path('books', views.LibraryList.as_view()),
    path('book/<int:pk>', views.SingleLibraryView.as_view()),
]
