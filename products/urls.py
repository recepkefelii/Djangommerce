from django.urls import path
from .views import ProductAPIView



urlpatterns = [
    path('create/',ProductAPIView.as_view(), name='product_create')
]
