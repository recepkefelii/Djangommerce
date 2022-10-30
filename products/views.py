from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status,permissions
from .models import Products
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.request import Request
from django.contrib.auth.models import User
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ProductList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['name','status']
    search_fields = ['name','status']
    ordering_fields = ['name','status']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(auth=self.request.user)
        

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(auth=self.request.user)

class ProductAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(auth=self.request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def get(self,request):
        product = Products.objects.all()
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data)

    def put(self,request,pk):
        product = Products.objects.get(pk=pk)
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        product = Products.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ProductCreate(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(auth=self.request.user)
    
class ProductUpdate(generics.UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(auth=self.request.user)
    
class ProductDelete(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(auth=self.request.user)
    
    
# Path: Ecommerce\products\serializers.py


   
# Path: Ecommerce\products\urls.py
# Compare this snippet from Ecommerce\shops\urls.py:



