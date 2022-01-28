import sys
from unicodedata import decimal
from django.shortcuts import render, redirect
from . models import Customer, Invoice, InvoiceItem, Company, TaxCodes
from . forms import CustomerForm, InvoiceItemForm
import django_tables2 as tables
from django.db.models import Sum

from .tables import CustomerTable, InvoiceItemsTable
# Create your views here.


def home(request):

    customers = Customer.objects.all()
    invoices = Invoice.objects.all()
    total_customers = customers.count()
    context = {'customers': customers, 'invoices': invoices,
               'total_customers': total_customers}

    return render(request, 'dashboard.html', context)


def customer(request, pk):
    customer = Customer.objects.get(customerID=pk)
    invoices=Invoice.objects.filter(customerID=pk)
    print(invoices)
    context = {'customer': customer, 'invoices':invoices}
    return render(request, 'customer.html', context)


def create_customer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, 'create_customer.html', context)

def updateCustomer(request,pk):
    customer=Customer.objects.get(customerID = pk)
    form = CustomerForm(instance=customer)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid:
            form.save()
            return redirect("/")
    
    context = {"form": form}
    return render(request, 'update_customer.html', context)

def deleteCustomer (request,pk):
    item = Customer.objects.get(customerID=pk)
    if request.method=="POST":
        item.delete()
        #field_value# = getattr(item, "invoiceID")
        return redirect("/")
    
    
    return render(request, "delete.html",{"obj":item})


def customers(request):
    table = CustomerTable(Customer.objects.all())
    return render(request, 'customers.html', {"table": table})


def invoice(request, pk):

    invoice = Invoice.objects.get(invoiceID=pk)
    custid = invoice.customerID.customerID
    customer = Customer.objects.get(customerID=custid)
    invoiceitems= InvoiceItem.objects.filter(invoiceID=pk)

    #print(invoice)
    subtotal= invoiceitems.aggregate(Sum('quantity'))
    print(subtotal)
    
    context = {'customer': customer, 'invoice': invoice, 'invoiceitems':invoiceitems }  #'invoiceitems':invoice.invoice_items

    return render(request, 'invoice.html', context)

    #table = InvoiceItemsTable(InvoiceItem.objects.all())
    # return render(request, 'customers.html', {"table": table})


def invoiceItems(request, cid):
    table = InvoiceItemsTable(InvoiceItem.objects.all())
    return render(request, 'customers.html', {"table": table})


def createInvoiceItem(request,invid):
    form = InvoiceItemForm(initial={'invoiceID':invid })
    form.fields['invoiceID'].widget.attrs['hidden'] = 'hidden'
    #form.fields['invoiceID'].disabled=True
    if request.method == "POST":
        form = InvoiceItemForm(request.POST)
        if form.is_valid:
           
            form.save()
            return redirect("invoice", pk=invid)

    context = {"form": form}
    return render(request, 'create_invoice_item.html', context)


def updateinvoiceItem(request,pk):
    item = InvoiceItem.objects.get(id=pk)
    form = InvoiceItemForm(instance=item)
    form.fields['invoiceID'].widget.attrs['hidden'] = 'hidden'
    #form.fields['invoiceID'].disabled=True
    

    if request.method == "POST":
        form = InvoiceItemForm(request.POST, instance=item)
        try:

            if form.is_valid:
                form.save()
                field_value = getattr(item, "invoiceID")

                return redirect("invoice",pk=field_value)
        except:
            print(sys.exc_info()[0])

    context = {"form": form}
    return render(request, 'update_invoice_item.html', context)

def deleteInvoiceItem (request,pk):
    item = InvoiceItem.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        field_value = getattr(item, "invoiceID")
        return redirect("invoice",pk=field_value)
    
    
    return render(request, "delete.html",{"obj":item})



def company(request):
    companies = Company.objects.all()
    return render(request, 'company.html', {'company': companies})


def hello_invo(request):
    return render(request, 'hello.html', {})
