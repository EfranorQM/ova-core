from rest_framework import serializers
from ova_core.models import Usuario, Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre']  # Devuelve solo el ID y el nombre

class UsuarioSerializer(serializers.ModelSerializer):
    rol = serializers.PrimaryKeyRelatedField(queryset=Rol.objects.all())  # Solo usa el ID del rol

    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email', 'contrasena', 'rol']
