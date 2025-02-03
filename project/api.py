    
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ProjectSerializers
from .models import Project
import cloudinary.uploader

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        # Si la solicitud tiene un archivo de imagen
        if 'photo' in self.request.FILES:
            # Subir la imagen a Cloudinary
            photo = self.request.FILES['photo']
            upload_result = cloudinary.uploader.upload(photo)
            
            # Obtener la URL de la imagen subida
            photo_url = upload_result['secure_url']
            
            # Crear el proyecto con la URL de la imagen
            serializer.save(photo_url=photo_url)
        else:
            # Si no hay imagen, se guarda el objeto sin foto
            serializer.save()
