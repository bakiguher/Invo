from . models import Customer, Invoice, InvoiceItem, Company, TaxCodes
import django_tables2 as tables

# Create your views here.

class CustomerTable(tables.Table):
    class Meta:
        model = Customer
        template_name="django_tables2/bootstrap4.html"
        


class InvoiceItemsTable(tables.Table):
    class Meta:
        model = InvoiceItem
        template_name="django_tables2/bootstrap4.html"

