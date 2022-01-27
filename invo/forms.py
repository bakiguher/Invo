from django.forms import ModelForm
from . models import Customer, Invoice, InvoiceItem, Company, TaxCodes


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


