from rest_framework import serializers
from .models import CustomUser, Resume
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # You can add custom claims here if needed
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        return {
            "status": 200,
            "message": "User logged in successfully",
            "data": {
                "refresh": data["refresh"],
                "access": data["access"],
            }
        }
class ResumeSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)
    class Meta:
        model = Resume
        fields = ['id', 'file', 'status', 'submitted_at']
        read_only_fields = ['status', 'submitted_at']

    def create(self, validated_data):
        return Resume.objects.create(**validated_data)

class ResumeReviewSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=[('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected')])
