from rest_framework import serializers
from .models import Shops


class ShopSerializer(serializers.ModelSerializer):
    hr_shops = serializers.CharField(source='shops.name',read_only=True)
    hr_auth = serializers.CharField(source='auth.username',read_only=True)
    class Meta:
        model = Shops
        fields = ['id','name','address','status','auth','hr_shops','hr_auth',]
    
    def create(self, validated_data):
        return Shops.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.status = validated_data.get('status', instance.status)
        instance.auth = validated_data.get('auth', instance.auth)
        instance.save()
        return instance
    

        

        