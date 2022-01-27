# Generated by Django 4.0.1 on 2022-01-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invo', '0006_rename__amount_invoiceitem_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('address1', models.CharField(blank=True, max_length=255, null=True)),
                ('address2', models.CharField(blank=True, max_length=255, null=True)),
                ('address3', models.CharField(blank=True, max_length=255, null=True)),
                ('address4', models.CharField(blank=True, max_length=255, null=True)),
                ('companyID', models.IntegerField()),
                ('taxNumber', models.CharField(max_length=50)),
                ('logoLocation', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='invoiceitem',
            old_name='amount',
            new_name='_amount',
        ),
        migrations.RemoveField(
            model_name='invoiceitem',
            name='finalAmount',
        ),
    ]
