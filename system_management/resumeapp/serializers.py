
from rest_framework import serializers
from .models import Resume
import os

class ResumeSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)

    class Meta:
        model = Resume
        fields = ['id', 'file', 'status', 'submitted_at']
        read_only_fields = ['status', 'submitted_at']

    def validate_file(self, value):
        allowed_mime_types = [
            'application/pdf',
            'application/msword',  # .doc
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document'  # .docx
        ]
        if value.content_type not in allowed_mime_types:
            raise serializers.ValidationError("Only PDF or Word documents (.pdf, .doc, .docx) are allowed.")

        ext = os.path.splitext(value.name)[1].lower()
        if ext not in ['.pdf', '.doc', '.docx']:
            raise serializers.ValidationError("File extension not allowed.")

        return value

class ResumeReviewSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=[('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected')])

    def to_internal_value(self, data):
        # Normalize status to uppercase before validation
        if 'status' in data and isinstance(data['status'], str):
            data['status'] = data['status'].upper()
        return super().to_internal_value(data)

    def validate(self, attrs):
        resume = self.instance
        if resume.status != 'PENDING':
            raise serializers.ValidationError("Resume has already been reviewed and cannot be changed again.")
        return attrs

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance
