from django.urls import path
from .views import ProductAPIView
from .views import ProductList
from .views import ProductDetail
from .views import ProductUpdate
from .views import ProductDelete
from .views import ProductCreate






urlpatterns = [
    path('create/',ProductAPIView.as_view(), name='product_create'),
    path('list/',ProductList.as_view(), name='product_list'),
    path('detail/<int:pk>/',ProductDetail.as_view(), name='product_detail'),
    path('update/<int:pk>/',ProductUpdate.as_view(), name='product_update'),
    path('delete/<int:pk>/',ProductDelete.as_view(), name='product_delete'),
    path('create/',ProductCreate.as_view(), name='product_create'),
    
]
