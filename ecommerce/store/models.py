from email.mime import image
from itertools import product
from pickle import TRUE
from typing_extensions import Self
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name= 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
        
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)


def __str__(self):
    return self.name

class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price=models.FloatField(max_length=200,null=True)
    digital=models.BooleanField(default=False,null=True,blank=False)
    image=models.ImageField(upload_to="products/%Y/%m/%d",blank=True)
    
    def __str__(self):
        return self.name

    
    
    
    
    