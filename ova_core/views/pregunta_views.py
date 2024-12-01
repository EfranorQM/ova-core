from rest_framework.viewsets import ModelViewSet
from ova_core.models import Pregunta
from ova_core.serializers.pregunta_serializer import PreguntaSerializer

class PreguntaViewSet(ModelViewSet):
    """
    ViewSet para manejar Preguntas.
    Filtra las preguntas por actividad si se pasa el parámetro 'actividad_id'.
    """
    serializer_class = PreguntaSerializer

    def get_queryset(self):
        """
        Filtra las preguntas por actividad si se proporciona 'actividad_id'.
        """
        actividad_id = self.request.query_params.get('actividad_id')
        if actividad_id:
            return Pregunta.objects.filter(actividad_id=actividad_id)
        return Pregunta.objects.all()
