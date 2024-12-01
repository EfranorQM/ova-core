from rest_framework.viewsets import ModelViewSet
from ova_core.models import Resultado
from ova_core.serializers.resultado_serializer import ResultadoSerializer

class ResultadoViewSet(ModelViewSet):
    """
    ViewSet para manejar Resultados.
    Filtra los resultados por usuario o actividad si se pasan los parámetros 'usuario_id' o 'actividad_id'.
    """
    serializer_class = ResultadoSerializer

    def get_queryset(self):
        """
        Filtra los resultados por usuario o actividad si se proporcionan 'usuario_id' o 'actividad_id'.
        """
        usuario_id = self.request.query_params.get('usuario_id')
        actividad_id = self.request.query_params.get('actividad_id')
        queryset = Resultado.objects.all()

        if usuario_id:
            queryset = queryset.filter(usuario_id=usuario_id)
        if actividad_id:
            queryset = queryset.filter(actividad_id=actividad_id)

        return queryset
