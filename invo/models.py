from django.db import models

# Create your models here.


class Company(models.Model):
    companyName = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    address3 = models.CharField(max_length=255, null=True, blank=True)
    address4 = models.CharField(max_length=255, null=True, blank=True)
    companyID = models.IntegerField()
    taxNumber = models.CharField(max_length=50)
    logoLocation = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.companyName


class Customer(models.Model):
    customerID = models.BigAutoField(primary_key=True)
    customerName = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    fax = models.CharField(max_length=50, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    isDeleted = models.BooleanField()
    billingAddress1 = models.CharField(max_length=255, null=True, blank=True)
    billingAddress2 = models.CharField(max_length=255, null=True, blank=True)
    billingAddress3 = models.CharField(max_length=255, null=True, blank=True)
    taxNumber = models.CharField(max_length=50)
    def __str__(self):
        return self.customerName


class Invoice(models.Model):
    invoiceID = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=50)
    currencyCode = models.CharField(max_length=20)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    dueBy = models.DateField(null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    companyID = models.IntegerField()
    note = models.CharField(max_length=2000)

    class Meta:
        ordering = ('-date', 'invoiceID')

    def __str__(self):
        return str(self.invoiceID)



    # subTotal = models.DecimalField(max_digits=10, decimal_places=2)
    # taxName1 = models.CharField(max_length=20)
    # totalTax1 = models.DecimalField(max_digits=10, decimal_places=2)
    # taxName2 = models.CharField(max_length=20)
    # totalTax2 = models.DecimalField(max_digits=10, decimal_places=2)
    # taxName3 = models.CharField(max_length=20)
    # totalTax3 = models.DecimalField(max_digits=10, decimal_places=2)
    # total = models.DecimalField(max_digits=10, decimal_places=2)


class TaxCodes(models.Model):
    taxCode = models.CharField(primary_key=True, max_length=20)
    taxPercent = models.DecimalField(max_digits=2, decimal_places=2)
    def __str__(self):
        return self.taxCode


class InvoiceItem(models.Model):
    invoiceID = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    seq = models.IntegerField()
    itemDescription = models.CharField(max_length=1000)
    taxCode = models.ManyToManyField(TaxCodes)
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        #x=self.invoiceID #+ " " + str(self.seq)
        return str(self.invoiceID.code)  + " / " + str(self.id )


