from rest_framework import serializers
from ova_core.models import Progreso

class ProgresoSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.CharField(source='usuario.nombre', read_only=True)  # Muestra el nombre del usuario
    leccion_titulo = serializers.CharField(source='leccion.titulo', read_only=True)  # Muestra el título de la lección

    class Meta:
        model = Progreso
        fields = '__all__'  # Incluye todos los campos del modelo
        extra_fields = ['usuario_nombre', 'leccion_titulo']  # Campos adicionales para relaciones
