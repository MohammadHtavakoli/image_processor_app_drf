from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ProcessedImage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ProcessedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessedImage
        fields = ('id', 'user', 'original_image', 'processed_image', 'created_at')
        read_only_fields = ('user', 'processed_image', 'created_at')