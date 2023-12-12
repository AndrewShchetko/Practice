from rest_framework import serializers
from .models import Images


class ImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField
    
    class Meta:
        model = Images
        fields = ['image', 'comment']
