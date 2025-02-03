from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    character = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    photo = CloudinaryField('image')

    def __str__(self):
        return self.name