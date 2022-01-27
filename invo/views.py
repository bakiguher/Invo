from django.shortcuts import render
from . models import Customer, Invoice, InvoiceItem, Company, TaxCodes
from . forms import CustomerForm
import django_tables2 as tables

from .tables import CustomerTable
# Create your views here.




def hello_invo(request):
    return render(request, 'hello.html', {})


def customers(request):
    table = CustomerTable(Customer.objects.all())
    return render(request, 'customers.html', {"table": table})


def create_customer(request):
    form=CustomerForm()
    if request.method == "POST":
        form=CustomerForm(request.POST)
        if form.is_valid:
            form.save()

    context={"form":form}
    return render(request, 'create_customer.html',context)




def company(request):
    companies = Company.objects.all()
    return render(request, 'company.html', {'company': companies})






def customers2(request):
    customer = Customer.objects.all()
    form = CustomerForm(instance=customer)
    context={"form":form}

    return render(request, "customers.html", context)

    # topics=Topic.objects.all()

    
    # if request.method == "POST":
    #     topic_name=request.POST.get('topic')
    #     topic, created=Topic.objects.get_or_create(name=topic_name)
    #     form=RoomForm(request.POST, instance=room)
    #     room.name=request.POST.get('name')
    #     room.topic=topic
    #     room.description=request.POST.get('description')
    #     room.save()
    #     return redirect("home")
    # context = {"form":form, "topics":topics, 'room':room}
    # return render(request, "base/room_form.html", context)