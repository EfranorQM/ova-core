from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include

def home(request):
    return HttpResponse("Bienvenido a la API OVA")

urlpatterns = [
    path('', home),  # Ruta para la raíz
    path('admin/', admin.site.urls),
    path('api/', include('ova_core.urls')),  # Incluye las rutas del router
]
