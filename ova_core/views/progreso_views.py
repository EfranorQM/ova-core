from rest_framework.viewsets import ModelViewSet
from ova_core.models import Progreso
from ova_core.serializers.progreso_serializer import ProgresoSerializer

class ProgresoViewSet(ModelViewSet):
    """
    ViewSet para manejar el Progreso.
    Filtra el progreso por usuario o lección si se pasan los parámetros 'usuario_id' o 'leccion_id'.
    """
    serializer_class = ProgresoSerializer

    def get_queryset(self):
        """
        Filtra el progreso por usuario o lección si se proporcionan 'usuario_id' o 'leccion_id'.
        """
        usuario_id = self.request.query_params.get('usuario_id')
        leccion_id = self.request.query_params.get('leccion_id')
        queryset = Progreso.objects.all()

        if usuario_id:
            queryset = queryset.filter(usuario_id=usuario_id)
        if leccion_id:
            queryset = queryset.filter(leccion_id=leccion_id)

        return queryset
