# Generated by Django 4.0.1 on 2022-01-28 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invo', '0013_remove_invoice_subtotal_remove_invoice_taxname1_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoiceitem',
            options={'ordering': ('invoiceID', 'seq')},
        ),
    ]