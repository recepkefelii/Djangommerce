from email.policy import default
from turtle import mode
from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Shops(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    auth = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    image = models.ImageField()

    def __str__(self) -> str:
        return self.name
