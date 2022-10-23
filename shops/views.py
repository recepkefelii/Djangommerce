from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.request import Request
from .serializes import ShopSerializer
from .models import Shops
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ShopsCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ShopSerializer
    def post(self,request:Request):

        data = request.data
        user_id = request.user.id
        data['auth'] = user_id
        verificationStatus = request.user.verification

        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            
            if not verificationStatus:
                return Response(data={"Please verify your email"})
            serializer.save()
            message = {
            "mesage":'created shops',
            "data":serializer.data
            } 
            return Response(data=message,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request:Request):
        shop = Shops.objects.filter(auth=request.user)
        serializer = self.serializer_class(shop,many=True)
        
        return Response(data=serializer.data,status=status.HTTP_200_OK)


class ShopFilterAPIView(generics.ListAPIView):
    queryset = Shops.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    serializer_class = ShopSerializer
    search_fields = ['name','shops__name','auth__username']
    filterset_fields = ['name', 'auth']
    #http://127.0.0.1:8000/shop/filter/?auth=4
    #http://127.0.0.1:8000/shop/filter/?name=shop_name
