from rest_framework import serializers
from ova_core.models import Actividad

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'  # Incluye todos los campos del modelo
