"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include           # import include
# from django.contrib import admin              # comment out, or just delete
urlpatterns = [
    # path('admin/', admin.sites.urls),         # comment out, or just delete
    # path('', include('app1.urls')),
    #path('app2/', include('app2.urls')),
    #path('time/', include('apptime.urls')),
    #path('app3/', include('app3.urls')),
    path('', include('app4.urls')),
    path('rword/', include('random_word.urls'))
    ]