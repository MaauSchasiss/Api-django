from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    character = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name