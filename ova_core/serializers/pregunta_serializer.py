from rest_framework import serializers
from ova_core.models import Pregunta

class PreguntaSerializer(serializers.ModelSerializer):
    actividad_titulo = serializers.CharField(source='actividad.titulo', read_only=True)  # Muestra el título de la actividad

    class Meta:
        model = Pregunta
        fields = '__all__'  # Incluye todos los campos del modelo
        extra_fields = ['actividad_titulo']  # Campo adicional para el título de la actividad
