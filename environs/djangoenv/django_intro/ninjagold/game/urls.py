from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('process_money/<int:id>', views.play),
    path('reset', views.new),
    path('objectives', views.obje),
    path('winner',views.wins)
]