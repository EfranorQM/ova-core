from rest_framework import serializers
from ova_core.models import RecursoMultimedia

class RecursoMultimediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecursoMultimedia
        fields = '__all__'  # Incluye todos los campos del modelo
