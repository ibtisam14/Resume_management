from rest_framework import serializers
from .models import Resume

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
