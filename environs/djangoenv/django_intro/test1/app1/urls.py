from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('index', views.index),
    path('bears', views.one_method),                        # would only match localhost:8000/bears
    path('bears/<int:my_val>', views.another_method),       # would match localhost:8000/bears/23
    path('bears/<str:name>/poke', views.yet_another),       # would match localhost:8000/bears/pooh/poke
    path('bears/<int:id>/<str:color>', views.one_more)         # would match localhost:8000/17/brown
]
