from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['username'] = user.username
        token['is_admin'] = user.is_admin
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        return {
            "status": 200,
            "message": "User logged in successfully",
            "data": {
                "email": self.user.email,
                "username": self.user.username,
                "access_token": data["access"],
                "refresh_token": data["refresh"]
            }
        }
