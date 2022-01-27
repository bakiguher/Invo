from django.contrib import admin
from django.conf import settings

from .models import Customer, Invoice, InvoiceItem, Company, TaxCodes

admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Company)
admin.site.register(TaxCodes)
# Register your models here.
