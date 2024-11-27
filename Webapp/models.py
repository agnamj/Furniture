from django.db import models

class contact_DB(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    lname = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    mobile = models.CharField(max_length=100,null=True,blank=True)
    message = models.CharField(max_length=100,null=True,blank=True)

class signup_db(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    cpassword = models.CharField(max_length=100,null=True,blank=True)

class cart_db(models.Model):
    username =  models.CharField(max_length=100,null=True,blank=True)
    productname = models.CharField(max_length=100,null=True,blank=True)
    totalprice = models.IntegerField(null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
class order_db(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    place = models.CharField(max_length=100,null=True,blank=True)
    Address = models.TextField(max_length=100,null=True,blank=True)
    pin = models.CharField(max_length=100,null=True,blank=True)
    Totalprice = models.CharField(max_length=100,null=True,blank=True)
    Message = models.CharField(max_length=100,null=True,blank=True)
