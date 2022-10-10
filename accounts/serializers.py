from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User
from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user


class SignUpSerializer(serializers.ModelSerializer):
    
    username=serializers.CharField(max_length=45)
    
    class Meta:
        model = User
        fields = ['email','username','password','verification','verificationCode','seller']

    def validate(self, attrs):

        email_exists = User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError("Bu email ile hesap oluşturulmuş")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

        

        return user


class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=80)
    password=serializers.CharField(min_length=8,write_only=True)
    verification=serializers.BooleanField(default=False)

    def validate(self, attrs):
        
        user = authenticate(email=attrs['email'], password=attrs['password'])


        if not user:
            raise serializers.ValidationError("hatalı giriş")
        
        
        tokens = create_jwt_pair_for_user(user)

        attrs['token'] = tokens
        return attrs

class EmailVerificationSerializer(serializers.Serializer):
    verificationCode = serializers.CharField()








