from statistics import mode
from django.db import models
from categories.basemodel.base import BaseModel
from categories.models import Categories

class Products(BaseModel):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    description = models.CharField(max_length=150)
    category = models.OneToOneField(Categories,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/',null=True)
    