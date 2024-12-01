from rest_framework import serializers
from ova_core.models import Modulo

class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = '__all__'  # Incluye todos los campos del modelo
