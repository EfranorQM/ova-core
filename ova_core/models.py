from django.db import models


class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Roles'
        
    def __str__(self):
        return self.nombre  # Esto mostrará el nombre del rol en lugar de "Rol object"


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='usuarios')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Usuarios'
    
    def __str__(self):
        return self.nombre

class Modulo(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    orden = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Modulos'
    
    def __str__(self):
        return self.titulo


class Leccion(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name='lecciones')
    titulo = models.CharField(max_length=255)
    contenido = models.TextField(blank=True, null=True)
    orden = models.IntegerField()

    class Meta:
        db_table = 'Lecciones'
    
    def __str__(self):
        return self.titulo


class RecursoMultimedia(models.Model):
    TIPOS = [
        ('video', 'Video'),
        ('imagen', 'Imagen'),
        ('documento', 'Documento'),
        ('grafico', 'Gráfico'),
    ]
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name='recursos')
    tipo = models.CharField(max_length=20, choices=TIPOS)
    url = models.URLField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'RecursosMultimedia'


class Actividad(models.Model):
    TIPOS = [
        ('interactiva', 'Interactiva'),
        ('evaluacion', 'Evaluación'),
    ]
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name='actividades')
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPOS)

    class Meta:
        db_table = 'Actividades'
    
    def __str__(self):
        return self.titulo


class Pregunta(models.Model):
    TIPOS = [
        ('opcion_multiple', 'Opción Múltiple'),
        ('verdadero_falso', 'Verdadero/Falso'),
        ('respuesta_abierta', 'Respuesta Abierta'),
    ]
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name='preguntas')
    pregunta = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPOS)

    class Meta:
        db_table = 'Preguntas'
    
    def __str__(self):
        return self.pregunta


class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    texto = models.TextField()
    es_correcta = models.BooleanField()

    class Meta:
        db_table = 'Opciones'


class Resultado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='resultados')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name='resultados')
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fecha_completado = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Resultados'


class Progreso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='progresos')
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name='progresos')
    completado = models.BooleanField(default=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Progreso'


class Configuracion(models.Model):
    clave = models.CharField(max_length=50, unique=True)
    valor = models.TextField()

    class Meta:
        db_table = 'Configuraciones'
