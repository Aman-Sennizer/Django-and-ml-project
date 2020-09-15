from django.urls import path
from Index import views
urlpatterns = [

    path('', views.home, name='home'),
    path('home', views.home, name='home'),



    ]
