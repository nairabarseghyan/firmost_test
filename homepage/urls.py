from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('gym/', views.gym, name="gym"),
]
