from django.urls import path
from . import views

urlpatterns = [
    path('blogs', views.BlogList.as_view()),
    path('blog/<int:pk>', views.SingleBlogView.as_view()),
]
