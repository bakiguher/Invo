from django.urls import path
from invo import views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('customers/', views.customers, name='customers') ,
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_customer/', views.create_customer, name='create_customer'),
    path('invoice/<str:pk>/', views.invoice, name="invoice"),
    path('create_invoice_item/<str:invid>', views.createInvoiceItem, name='create_invoice_item'),
    path('update_customer/<str:pk>/', views.updateCustomer, name="update_customer"),
    path('delete_customer/<str:pk>/', views.deleteCustomer, name="delete_customer"),
    
    
    path('create_invoice/', views.createInvoice, name='create_invoice'),
    
    
    path('delete_invoice_item/<str:pk>/', views.deleteInvoiceItem, name="delete_invoice_item"),
    path('update_invoice_item/<str:pk>/', views.updateinvoiceItem, name="update_invoice_item"),
    



    
    
]

