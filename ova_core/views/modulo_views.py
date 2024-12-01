from rest_framework.viewsets import ModelViewSet
from ova_core.models import Modulo
from ova_core.serializers.modulo_serializer import ModuloSerializer

class ModuloViewSet(ModelViewSet):
    """
    ViewSet para manejar Módulos Educativos de forma automática.
    """
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer
