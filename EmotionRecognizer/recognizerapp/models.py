from django.db import models


class Images(models.Model):
    image = models.ImageField(upload_to='%Y/%m/%d')
    comment = models.CharField(max_length=255, blank=True)
