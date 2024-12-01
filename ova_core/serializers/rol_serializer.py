from rest_framework import serializers
from ova_core.models import Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'  # Incluye todos los campos del modelo
