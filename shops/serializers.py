from rest_framework import serializers
from .models import Shops
class ShopSerializer(serializers.ModelSerializer):
    hr_shops = serializers.CharField(source='shops.name',read_only=True)
    hr_auth = serializers.CharField(source='auth.username',read_only=True)
    class Meta:
        model = Shops
        fields = ['id','name','address','status','auth','hr_shops','hr_auth',]

        