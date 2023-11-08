from django.db import models
from django.contrib.auth.models import User
from recognizerapp.models import Images


class Results(models.Model):
    image = models.OneToOneField(Images, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=40)
    user = models.CharField(max_length=100)
