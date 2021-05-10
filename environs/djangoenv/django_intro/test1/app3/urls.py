from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homes),
    path('doit', views.doit)
]