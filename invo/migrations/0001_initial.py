# Generated by Django 4.0.1 on 2022-01-27 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerID', models.BigAutoField(primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('fax', models.CharField(blank=True, max_length=50, null=True)),
                ('createdDate', models.DateField()),
                ('isDeleted', models.BooleanField()),
                ('billingAddress1', models.CharField(blank=True, max_length=255, null=True)),
                ('billingAddress2', models.CharField(blank=True, max_length=255, null=True)),
                ('billingAddress3', models.CharField(blank=True, max_length=255, null=True)),
                ('taxNumber', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoiceID', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50)),
                ('currencyCode', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('dueBy', models.DateField()),
                ('subTotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('taxName1', models.CharField(max_length=20)),
                ('totalTax1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('taxName2', models.CharField(max_length=20)),
                ('totalTax2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('taxName3', models.CharField(max_length=20)),
                ('totalTax3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('createdDate', models.DateField()),
                ('companyID', models.IntegerField()),
                ('note', models.CharField(max_length=2000)),
                ('customerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invo.customer')),
            ],
        ),
    ]