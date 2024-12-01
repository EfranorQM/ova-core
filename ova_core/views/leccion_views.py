from rest_framework.viewsets import ModelViewSet
from ova_core.models import Leccion
from ova_core.serializers.leccion_serializer import LeccionSerializer

class LeccionViewSet(ModelViewSet):
    """
    ViewSet para manejar Lecciones.
    Filtra las lecciones por módulo si se pasa el parámetro 'modulo_id'.
    """
    serializer_class = LeccionSerializer

    def get_queryset(self):
        """
        Filtra las lecciones por módulo si se proporciona 'modulo_id' como parámetro.
        """
        modulo_id = self.request.query_params.get('modulo_id')
        if modulo_id:
            return Leccion.objects.filter(modulo_id=modulo_id)
        return Leccion.objects.all()
