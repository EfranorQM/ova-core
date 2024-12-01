from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ova_core.models import Usuario

class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        contrasena = request.data.get("contrasena")

        # Verificar si el usuario existe
        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Comparar la contraseña directamente
        if usuario.contrasena != contrasena:
            return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_401_UNAUTHORIZED)

        # Si las credenciales son correctas, devolver datos del usuario
        return Response({
            "id": usuario.id,
            "nombre": usuario.nombre,
            "email": usuario.email,
            "rol": usuario.rol.nombre  # Incluye el nombre del rol
        }, status=status.HTTP_200_OK)
