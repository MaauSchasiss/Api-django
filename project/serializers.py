from rest_framework import serializers
from .models import project

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ('id', 'name', 'age', 'character', 'rol', 'photo')
        read_only_fields = ('photo',)