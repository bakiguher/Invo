from django.urls import path
from invo import views

urlpatterns = [
    path('', views.hello_invo, name='hello'),


    
]

