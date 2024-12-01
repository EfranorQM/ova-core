from rest_framework import serializers
from ova_core.models import Configuracion

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = '__all__'  # Incluye todos los campos del modelo
