from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
         abstract = True