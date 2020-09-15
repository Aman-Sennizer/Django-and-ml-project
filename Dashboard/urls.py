from django.urls import path
from Dashboard import views

urlpatterns = [

    path('Dashboard', views.dashboard, name='Dashboard'),
    path('logout', views.logoutuser, name='logout'),

    ]
