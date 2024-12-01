from rest_framework.routers import DefaultRouter
from ova_core.views.rol_views import RolViewSet
from ova_core.views.usuario_views import UsuarioViewSet
from ova_core.views.modulo_views import ModuloViewSet
from ova_core.views.leccion_views import LeccionViewSet
from ova_core.views.actividad_views import ActividadViewSet
from ova_core.views.recurso_multimedia_views import RecursoMultimediaViewSet
from ova_core.views.pregunta_views import PreguntaViewSet
from ova_core.views.opcion_views import OpcionViewSet
from ova_core.views.resultado_views import ResultadoViewSet
from ova_core.views.progreso_views import ProgresoViewSet
from ova_core.views.configuracion_views import ConfiguracionViewSet
from ova_core.views.login_views import LoginView  # Vista personalizada para login
from django.urls import path, include  # Import necesario

# Configuración del DefaultRouter
router = DefaultRouter()
router.register(r'roles', RolViewSet, basename='rol')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'modulos', ModuloViewSet, basename='modulo')
router.register(r'lecciones', LeccionViewSet, basename='leccion')
router.register(r'actividades', ActividadViewSet, basename='actividad')
router.register(r'recursos-multimedia', RecursoMultimediaViewSet, basename='recurso-multimedia')
router.register(r'preguntas', PreguntaViewSet, basename='pregunta')
router.register(r'opciones', OpcionViewSet, basename='opcion')
router.register(r'resultados', ResultadoViewSet, basename='resultado')
router.register(r'progreso', ProgresoViewSet, basename='progreso')
router.register(r'configuraciones', ConfiguracionViewSet, basename='configuracion')

# Definir las rutas personalizadas
urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),  # Ruta personalizada de login
    path('', include(router.urls)),  # Rutas generadas automáticamente por el router
]
