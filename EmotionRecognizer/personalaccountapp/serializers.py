from rest_framework import serializers
from .models import Results, User
from recognizerapp.serializers import ImagesSerializer


class ResultsSerializer(serializers.ModelSerializer):
    image = ImagesSerializer()

    class Meta:
        model = Results
        fields = ['image', 'emotion']


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
