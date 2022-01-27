from django.urls import path
from invo import views

urlpatterns = [
    path('', views.hello_invo, name='hello'),
    path('customers/', views.customers, name='customers') ,
    path('create_customer/', views.create_customer, name='create_customers') ,
    
]

