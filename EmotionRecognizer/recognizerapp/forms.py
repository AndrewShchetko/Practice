from django import forms
from .models import Images


class NeuralNetworkForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image', 'comment')
