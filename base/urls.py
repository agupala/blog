from django.urls import path
from . import views
from posts import views as posts_views

urlpatterns = [
    path('', posts_views.home, name="home"),
    path('about/', views.about, name="about"),
]