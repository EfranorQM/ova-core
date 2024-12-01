from rest_framework import serializers
from ova_core.models import Opcion

class OpcionSerializer(serializers.ModelSerializer):
    pregunta_texto = serializers.CharField(source='pregunta.pregunta', read_only=True)  # Muestra el texto de la pregunta

    class Meta:
        model = Opcion
        fields = '__all__'  # Incluye todos los campos del modelo
        extra_fields = ['pregunta_texto']  # Campo adicional para el texto de la pregunta
