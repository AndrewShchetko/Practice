from rest_framework import serializers
from .models import Results, User
from recognizerapp.serializers import ImagesSerializer


class ResultsSerializer(serializers.ModelSerializer):
    #image = ImagesSerializer()

    class Meta:
        model = Results
        fields = ['image', 'emotion', 'user']


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError("Passwords do not match")

        return data

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password1']

        user = User.objects.create_user(username=username, password=password)
        return user