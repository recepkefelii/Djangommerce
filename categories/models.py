from django.db import models
from .basemodel.base import BaseModel
from shops.models import Shops

class Categories(BaseModel):
    author = models.ForeignKey(Shops,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()



class SubCategories(BaseModel):
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()





