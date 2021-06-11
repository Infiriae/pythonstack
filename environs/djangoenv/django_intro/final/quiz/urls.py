from django.urls import path, include    
from . import views

urlpatterns = [
    path('', views.index),
    path('reg', views.register),
    path('success', views.success),
    path('login', views.login)
]