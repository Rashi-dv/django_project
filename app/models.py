from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

# Create your models here.
# register
class registerModels(models.Model):
    c_user=models.ForeignKey(User,on_delete=models.CASCADE)
    Tel_number = models.CharField(max_length=10)
    Address = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    destic = models.CharField(max_length=255)
    
    
# product Details
class productModels(models.Model):
    Prod_Id = models.IntegerField()
    prod_Name = models.CharField(max_length=255)
    Prod_Price = models.IntegerField()
    Prod_Desc = models.CharField(max_length=255)
    Prod_image = models.ImageField(upload_to='images/',blank=True)
    
    def __str__(self):
        return self.prod_Name
    
# cart

class cart_itemModel(models.Model):
    item = models.ForeignKey(productModels,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    is_order = models.BooleanField(default=True)

# user cart
class cartModel (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    item = models.ManyToManyField(cart_itemModel)