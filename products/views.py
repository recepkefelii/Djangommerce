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



class ProductAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request:Request):
        product = Products.objects.all()
        serializer = ProductSerializer(product,many=True) 
        return Response(data=serializer.data,status=status.HTTP_200_OK)
        
        

    def post(self,request:Request):
        data = request.data
        user = request.user
        seller = request.user.seller
        if not seller:
            return Response(data={"Please create shop"})
        serializer = ProductSerializer(data=data)
                
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
