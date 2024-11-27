from django.db import models

class Furniture_DB(models.Model):
    category_n = models.CharField(max_length=100,null=True,blank=True)
    category_image = models.ImageField(upload_to="category",null=True,blank=True)
    description = models.TextField(max_length=100,null=True,blank=True)

class product_DB(models.Model):
    category_name = models.CharField(max_length=100,null=True,blank=True)
    pro_name = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Mrp = models.IntegerField(null=True,blank=True)
    Description = models.TextField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    manufactured = models.CharField(max_length=100,null=True,blank=True)
    category_image1 = models.ImageField(upload_to="product",null=True,blank=True)
    category_image2 = models.ImageField(upload_to="product",null=True,blank=True)
    category_image3 = models.ImageField(upload_to="product",null=True,blank=True)


