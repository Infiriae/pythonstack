from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homes),
    path('submit', views.doit),
    path('results', views.done)
]