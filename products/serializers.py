from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'
    
    def create(self, validated_data):
        return Products.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
    


    

    


