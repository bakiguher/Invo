# Generated by Django 4.0.1 on 2022-01-27 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invo', '0005_rename_amount_invoiceitem__amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoiceitem',
            old_name='_amount',
            new_name='amount',
        ),
    ]
