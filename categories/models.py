from django.db import models
from .basemodel.base import BaseModel
from shops.models import Shops

class Categories(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()






