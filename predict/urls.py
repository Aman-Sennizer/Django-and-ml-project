from django.urls import path
from predict import views

app_name = 'predict'
urlpatterns = [

    path('predict/', views.predict, name="predict"),
    path('predictchances/', views.predict_chances, name='submit_prediction'),

]
