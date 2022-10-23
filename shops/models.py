from django.db import models

from django.contrib.auth import get_user_model

from categories.basemodel.base import BaseModel
User = get_user_model()


class Shops(BaseModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    auth = models.OneToOneField(User,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/',null=True)

    def __str__(self) -> str:
        return self.name

