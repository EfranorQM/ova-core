from rest_framework.viewsets import ModelViewSet
from ova_core.models import Usuario
from ova_core.serializers.usuario_serializer import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    """
    ViewSet para manejar Usuarios de forma automática.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
