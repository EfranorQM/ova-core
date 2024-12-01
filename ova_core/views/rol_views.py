from rest_framework.viewsets import ModelViewSet
from ova_core.models import Rol
from ova_core.serializers.rol_serializer import RolSerializer

class RolViewSet(ModelViewSet):
    """
    ViewSet para manejar roles de forma automática.
    """
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
