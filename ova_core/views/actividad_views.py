from rest_framework.viewsets import ModelViewSet
from ova_core.models import Actividad
from ova_core.serializers.actividad_serializer import ActividadSerializer

class ActividadViewSet(ModelViewSet):
    """
    ViewSet para manejar Actividades.
    Filtra las actividades por lección si se pasa el parámetro 'leccion_id'.
    """
    serializer_class = ActividadSerializer

    def get_queryset(self):
        """
        Filtra las actividades por lección si se proporciona 'leccion_id' como parámetro.
        """
        leccion_id = self.request.query_params.get('leccion_id')
        if leccion_id:
            return Actividad.objects.filter(leccion_id=leccion_id)
        return Actividad.objects.all()
