from django.db import models
from django.urls import reverse


class Gallery(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(null=True)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/images_gallery')

    def __str__(self):
        return self.title
