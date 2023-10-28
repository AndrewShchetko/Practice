from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ChangePasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class NeuralNetworkForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image', 'comment')
