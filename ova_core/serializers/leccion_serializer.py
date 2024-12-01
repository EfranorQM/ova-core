from rest_framework import serializers
from ova_core.models import Leccion

class LeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = '__all__'  # Incluye todos los campos del modelo
