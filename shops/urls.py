from django.urls import path
from .views import ShopsCreateView,ShopFilterAPIView
    

urlpatterns = [
    path('create/',ShopsCreateView.as_view(), name='create'),
    path('filter/',ShopFilterAPIView.as_view(), name='filter')
]

