from django.forms import ModelForm
from . models import Customer, Invoice, InvoiceItem, Company, TaxCodes


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('customerID', 'customerName',
                  'email',
                  'phone',
                  'fax',
                  'isDeleted',
                  'billingAddress1',
                  'billingAddress2',
                  'billingAddress3',
                  'taxNumber'
                  )


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ('invoiceID', 'code',
                  'currencyCode',
                  'customerID',
                  'date',
                  'dueBy',
                  'companyID',
                  'note'
                  )


class InvoiceItemForm(ModelForm):
    class Meta:
        model = InvoiceItem
        fields =('invoiceID', 'seq', 'itemDescription', 'taxCode', 'unitPrice', 'quantity')

    

    
