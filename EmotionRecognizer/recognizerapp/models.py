from django.contrib.auth.models import User
from django.db import models


class Images(models.Model):
    image = models.ImageField(upload_to='%Y/%m/%d')
    comment = models.CharField(max_length=255, blank=True)


class Results(models.Model):
    image = models.OneToOneField(Images, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=40)
    user = models.CharField(max_length=100)
