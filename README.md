# InVo
#### Video Demo:  https://youtu.be/6ReWyM_WCl4
#### Description:



**InVo** is an invoicing app with following features
- Invoice and bill for any product or service
- Include invoice due date
- Tax on item or total, inclusive or exclusive especially VAT tax

Frameworks used:
- Django
- Bootstrap
- django-tables2
- Database is sqlite3


Django is a high-level Python framework. It’s free and open source. It works with models, views, forms and urls. 
I developed the app in virtual enviroment with [virtualenv](https://virtualenv.pypa.io/en/latest/) tool

```
pip install virtualenv
virtualenv env
cd env
scripts\activate
django-admin startproject invoice
Python manage.py startapp invo
python manage.py runserver
```


Folder structure in vscode:

![image](https://user-images.githubusercontent.com/7795039/151625296-1bb0cc5a-ffd1-46c3-8360-658e65d36e8d.png)

Invoice is the name of the project. Invo is the name of an app in the project. Invo app settings are imported by Invoice Project. 

First I created my database models for Customer, Invoice, invoice Item. All the fields if not specified can not be null or blank. It was my first hassle. 
After creating the model I made the migrations. 
In urls I defined;
  -create
  -update
  -delete
for customer, invoice and invoice item.
Also for each operation I created a template html file. 

![image](https://user-images.githubusercontent.com/7795039/151625728-3e97d6e1-99db-4131-81cd-aecfd3ea69d5.png)

views.py file includes most of the code. 
Inserting, updating and deleting functions on orm design.
forms.py includes form classes I used mostly for updating data. The relationship betweein invoice and invoiceitems were easier with ModelForm of django.

```
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
```
I only had one static file and it was the logo. 

I used [bootstrap](https://getbootstrap.com/) for css.

In the project main folder I had 2 templates main.html and navbar.html. navbar.html extendded main.html and main.html is extended by every other html template
```
{% extends 'main.html' %}
```

One more code block I used in main.html is 
```
{% load humanize %}
````
when float data is rendered in html with 6 digits. Humanize package renders these kind of values to 2 decimal places. You define it in the code. 
```
        <td>{{item.tax|floatformat:2}}</td>
        <td>{{item.subTotal|floatformat:2}}</td>
        <td>{{item.total|floatformat:2}}</td>
```
In project settings folder I defined each app I used.

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_tables2',
    'semanticuiforms',
    'django_bootstrap5',
    'django.contrib.humanize',
    'invo',
]
```
---
**Future plans for Invo**

I will add reports
  - per customer
  - per period
  - per quarter

templates for invoices
  - different languages
  - printing to pdf
---
**Requirements**
```
asgiref==3.5.0 
autopep8==1.6.0 
beautifulsoup4==4.10.0 
Django==4.0.1 
django-bootstrap5==21.3
django-semanticui-forms==1.6.5
django-tables2==2.4.1
pycodestyle==2.8.0
soupsieve==2.3.1
sqlparse==0.4.2
toml==0.10.2
tzdata==2021.5
```
