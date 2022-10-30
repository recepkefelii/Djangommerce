from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.request import Request
from .serializers import ShopSerializer
from .models import Shops
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ShopList(generics.ListCreateAPIView):
    queryset = Shops.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'status']
    search_fields = ['name', 'status']
    ordering_fields = ['name', 'status']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(auth=self.request.user)
    

class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shops.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(auth=self.request.user)

class ShopAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(auth=self.request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def get(self,request):
        shop = Shops.objects.all()
        serializer = ShopSerializer(shop,many=True)
        return Response(serializer.data)

    def put(self,request,pk):
        shop = Shops.objects.get(pk=pk)
        serializer = ShopSerializer(shop,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        shop = Shops.objects.get(pk=pk)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    


        