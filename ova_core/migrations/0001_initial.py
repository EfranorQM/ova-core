# Generated by Django 5.1.2 on 2024-11-18 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Configuracion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("clave", models.CharField(max_length=50, unique=True)),
                ("valor", models.TextField()),
            ],
            options={
                "db_table": "Configuraciones",
            },
        ),
        migrations.CreateModel(
            name="Leccion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=255)),
                ("contenido", models.TextField(blank=True, null=True)),
                ("orden", models.IntegerField()),
            ],
            options={
                "db_table": "Lecciones",
            },
        ),
        migrations.CreateModel(
            name="Modulo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=255)),
                ("descripcion", models.TextField(blank=True, null=True)),
                ("orden", models.IntegerField()),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "Modulos",
            },
        ),
        migrations.CreateModel(
            name="Rol",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, unique=True)),
                ("descripcion", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "Roles",
            },
        ),
        migrations.CreateModel(
            name="Actividad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=255)),
                ("descripcion", models.TextField(blank=True, null=True)),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("interactiva", "Interactiva"),
                            ("evaluacion", "Evaluación"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "leccion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="actividades",
                        to="ova_core.leccion",
                    ),
                ),
            ],
            options={
                "db_table": "Actividades",
            },
        ),
        migrations.AddField(
            model_name="leccion",
            name="modulo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lecciones",
                to="ova_core.modulo",
            ),
        ),
        migrations.CreateModel(
            name="Pregunta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pregunta", models.TextField()),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("opcion_multiple", "Opción Múltiple"),
                            ("verdadero_falso", "Verdadero/Falso"),
                            ("respuesta_abierta", "Respuesta Abierta"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "actividad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="preguntas",
                        to="ova_core.actividad",
                    ),
                ),
            ],
            options={
                "db_table": "Preguntas",
            },
        ),
        migrations.CreateModel(
            name="Opcion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("texto", models.TextField()),
                ("es_correcta", models.BooleanField()),
                (
                    "pregunta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="opciones",
                        to="ova_core.pregunta",
                    ),
                ),
            ],
            options={
                "db_table": "Opciones",
            },
        ),
        migrations.CreateModel(
            name="RecursoMultimedia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("video", "Video"),
                            ("imagen", "Imagen"),
                            ("documento", "Documento"),
                            ("grafico", "Gráfico"),
                        ],
                        max_length=20,
                    ),
                ),
                ("url", models.URLField(max_length=255)),
                ("descripcion", models.TextField(blank=True, null=True)),
                (
                    "leccion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recursos",
                        to="ova_core.leccion",
                    ),
                ),
            ],
            options={
                "db_table": "RecursosMultimedia",
            },
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("contrasena", models.CharField(max_length=255)),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
                (
                    "rol",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="usuarios",
                        to="ova_core.rol",
                    ),
                ),
            ],
            options={
                "db_table": "Usuarios",
            },
        ),
        migrations.CreateModel(
            name="Resultado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "calificacion",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("fecha_completado", models.DateTimeField(auto_now_add=True)),
                (
                    "actividad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resultados",
                        to="ova_core.actividad",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resultados",
                        to="ova_core.usuario",
                    ),
                ),
            ],
            options={
                "db_table": "Resultados",
            },
        ),
        migrations.CreateModel(
            name="Progreso",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("completado", models.BooleanField(default=False)),
                ("fecha_actualizacion", models.DateTimeField(auto_now=True)),
                (
                    "leccion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="progresos",
                        to="ova_core.leccion",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="progresos",
                        to="ova_core.usuario",
                    ),
                ),
            ],
            options={
                "db_table": "Progreso",
            },
        ),
    ]