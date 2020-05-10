"""aurnag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('latlong/',views.get_latlong,name = "latlong"),
#     path('', views.signIn),
    path('audio/',views.audio,name="audio"),
    path('text1/',views.text1,name="text1"),
    path('text2/',views.text2,name="text2"),
    path('type/',views.type,name="type"),
    path('', views.signIn),
    path('signin', views.signIn, name="login"),
    path('postsign/', views.postsign, name="postsign"),
    path('logout/', views.logout, name="log"),
    path('postsignup/', views.postsignup, name='postsignup'),
    path('first_aid/', views.first_aid, name='firstaid'),
    path('savemylocation/', views.mylocation, name='savemylocation'),
    path('signup/', views.signUp, name="signup"),
    path('sharemylocation/',views.latlongi,name="sharemylocation"),
    path('latlongi', views.notify_emergencycontact, name="get_Location"),
    #path('latlong/', views.get_latlong, name="latlong")


]
