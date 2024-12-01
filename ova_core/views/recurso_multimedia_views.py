from rest_framework.viewsets import ModelViewSet
from ova_core.models import RecursoMultimedia
from ova_core.serializers.recurso_multimedia_serializer import RecursoMultimediaSerializer

class RecursoMultimediaViewSet(ModelViewSet):
    """
    ViewSet para manejar Recursos Multimedia de forma automática.
    """
    serializer_class = RecursoMultimediaSerializer

    def get_queryset(self):
        """
        Filtra los recursos multimedia por lección si se pasa el parámetro 'leccion_id'.
        """
        leccion_id = self.request.query_params.get('leccion_id')
        if leccion_id:
            return RecursoMultimedia.objects.filter(leccion_id=leccion_id)
        return RecursoMultimedia.objects.all()
