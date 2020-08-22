from django.db import models
from django.urls import reverse


class Sketches(models.Model):
    title = models.CharField(max_length=50)
    TYPE = (
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
        ('Used', 'Used')
    )
    type = models.CharField(max_length=50, null=True, choices=TYPE)
    date = models.DateField(null=True)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/images_sketches')

    def __str__(self):
        return self.title
