from rest_framework.viewsets import ModelViewSet
from ova_core.models import Opcion
from ova_core.serializers.opcion_serializer import OpcionSerializer

class OpcionViewSet(ModelViewSet):
    """
    ViewSet para manejar Opciones de Preguntas.
    Filtra las opciones por pregunta si se pasa el parámetro 'pregunta_id'.
    """
    serializer_class = OpcionSerializer

    def get_queryset(self):
        """
        Filtra las opciones por pregunta si se proporciona 'pregunta_id'.
        """
        pregunta_id = self.request.query_params.get('pregunta_id')
        if pregunta_id:
            return Opcion.objects.filter(pregunta_id=pregunta_id)
        return Opcion.objects.all()
