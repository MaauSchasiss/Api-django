from rest_framework import serializers
from .models import Project

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'age', 'character', 'rol', 'photo_url')
        read_only_fields = ('id',)