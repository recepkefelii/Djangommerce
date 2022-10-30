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

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
    
    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        super().get(*args, **kwargs)
    
    def get_all(self, *args, **kwargs):
        super().get_all(*args, **kwargs)
    
    def get_by_id(self, *args, **kwargs):
        super().get_by_id(*args, **kwargs)
    
    def get_by_name(self, *args, **kwargs):
        super().get_by_name(*args, **kwargs)
    
    def get_by_address(self, *args, **kwargs):
        super().get_by_address(*args, **kwargs)
    
    def get_by_status(self, *args, **kwargs):
        super().get_by_status(*args, **kwargs)
    
    def get_by_auth(self, *args, **kwargs):
        super().get_by_auth(*args, **kwargs)
    
    def get_by_date(self, *args, **kwargs):
        super().get_by_date(*args, **kwargs)
    
    def get_by_image(self, *args, **kwargs):
        super().get_by_image(*args, **kwargs)
        
