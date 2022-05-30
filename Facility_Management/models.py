# Create your models here.
from django.contrib.auth.models import User

from home.models import company_category, company_name
from django.db import models


class facility_management_client(models.Model):
    category = models.ForeignKey(company_category, on_delete=models.CASCADE)
    company_name = models.ForeignKey(company_name, on_delete=models.CASCADE)
    company_identity_code = models.CharField('Company Identity Code', max_length=10, unique=True)
    company_order_password = models.CharField('Company Order Password', max_length=50, unique=True)

    address = models.CharField('Location', max_length=200)
    contact = models.CharField('Contact', max_length=100)
    email = models.EmailField('Email', blank=True, null=True, max_length=200)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.company_identity_code


class facility_management_clients_login(models.Model):
    Id = models.IntegerField(primary_key=True, auto_created=True)
    category = models.CharField('Company Category', max_length=50)
    company_name = models.CharField('Company Name', max_length=50)
    company_identity_code = models.CharField('Company Identity Code', max_length=10)
    email = models.EmailField('Email', blank=True, null=True, max_length=200)
    client_login_address = models.GenericIPAddressField()
    contact = models.CharField('Contact', max_length=100)
    date_time_login = models.DateTimeField()
    date_time_logout = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class facility_management_service(models.Model):
    services_name = models.CharField('Enter Service Name', max_length=50)
    img = models.ImageField(upload_to=f'static\Our_Company\Services')
    about_service = models.TextField('About Service ', max_length=300)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.services_name


class facility_maincarodis(models.Model):
    name = models.CharField('name', max_length=200)
    img = models.ImageField(upload_to=f"static\Express_Facility_Management\maincaroselle")

    date_added = models.DateTimeField()

    def __str__(self):
        return self.name


class facilty_management_category(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    Facility_cate_name = models.CharField('Facility Category ', max_length=200)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.Facility_cate_name


class facilty_management_item(models.Model):
    item_cat = models.ForeignKey(facilty_management_category, on_delete=models.CASCADE)
    item_name = models.CharField('Item Name', max_length=200)
    price_per_a_quantity_bought = models.FloatField('Price per quantity bought', max_length=200)
    stocks = models.IntegerField()
    price_being_sold_for = models.FloatField('Price per quantity being sold', max_length=200)
    about_item = models.TextField('A brief note about the item', max_length=100)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.item_name


class facility_management_order(models.Model):
    cust_name =  models.CharField('Name of The Company', max_length=200)
    category = models.CharField('Company Category', max_length=200)
    datetime_local = models.DateTimeField()
    # ___________________________
    option1 = models.CharField('Order 1', max_length=50)
    quantity1 = models.CharField('Order 1 Quantity Wanted', max_length=50)
    # ____________________
    option2 = models.CharField('Order 2', max_length=50)
    quantity2 = models.CharField('Order 2 Quantity Wanted', max_length=50)
    # _______________________
    option3 = models.CharField('Order 3', max_length=50)
    quantity3 = models.CharField('Order 3 Quantity Wanted', max_length=50)
    # _______________________
    option4 = models.CharField('Order 4', max_length=50)
    quantity4 = models.CharField('Order 4 Quantity Wanted', max_length=50)
    # _______________________
    option5 = models.CharField('Order 5', max_length=50)
    quantity5 = models.CharField('Order 5 Quantity Wanted', max_length=50)
    # _______________________
    option6 = models.CharField('Order 6', max_length=50)
    quantity6 = models.CharField('Order 6 Quantity Wanted', max_length=50)
    # _______________________
    option7 = models.CharField('Order 7', max_length=50)
    quantity7 = models.CharField('Order 7 Quantity Wanted', max_length=50)
    # _______________________
    option8 = models.CharField('Order 8', max_length=50)
    quantity8 = models.CharField('Order 8 Quantity Wanted', max_length=50)
    # _______________________
    option9 = models.CharField('Order 9', max_length=50)
    quantity9 = models.CharField('Order 9 Quantity Wanted', max_length=50)
    # _______________________
    option10 = models.CharField('Order 10', max_length=50)
    quantity10 = models.CharField('Order 10 Quantity Wanted', max_length=50)
    # _______________________
    companyorderpassword = models.CharField('Company Order Password', max_length=50)
    message = models.TextField('A brief note about the item', max_length=100)
    read = models.BooleanField("Read", blank=True, null=True)
    order_done = models.BooleanField("Order sent to customer", blank=True, null=True)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.datetime_local
