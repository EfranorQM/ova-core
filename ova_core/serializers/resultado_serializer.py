from rest_framework import serializers
from ova_core.models import Resultado

class ResultadoSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.CharField(source='usuario.nombre', read_only=True)  # Muestra el nombre del usuario
    actividad_titulo = serializers.CharField(source='actividad.titulo', read_only=True)  # Muestra el título de la actividad

    class Meta:
        model = Resultado
        fields = '__all__'  # Incluye todos los campos del modelo
        extra_fields = ['usuario_nombre', 'actividad_titulo']  # Campos adicionales para relaciones
