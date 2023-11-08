from rest_framework import serializers
from .models import Results
from recognizerapp.serializers import ImagesSerializer

class ResultsSerializer(serializers.ModelSerializer):
    image = ImagesSerializer()

    class Meta:
        model = Results
        fields = ['image', 'emotion']
