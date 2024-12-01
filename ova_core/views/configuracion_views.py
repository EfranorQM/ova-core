from rest_framework.viewsets import ModelViewSet
from ova_core.models import Configuracion
from ova_core.serializers.configuracion_serializer import ConfiguracionSerializer

class ConfiguracionViewSet(ModelViewSet):
    """
    ViewSet para manejar Configuraciones del sistema.
    Permite buscar por clave.
    """
    serializer_class = ConfiguracionSerializer

    def get_queryset(self):
        """
        Permite filtrar las configuraciones por 'clave'.
        """
        clave = self.request.query_params.get('clave')
        queryset = Configuracion.objects.all()
        if clave:
            queryset = queryset.filter(clave=clave)
        return queryset