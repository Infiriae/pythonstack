from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.root),
    path('gen', views.doit),
    path('rset', views.flushout)
]