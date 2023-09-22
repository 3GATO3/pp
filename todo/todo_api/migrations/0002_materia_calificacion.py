# Generated by Django 4.1 on 2023-09-22 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("todo_api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Materia",
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
                ("claveMateria", models.CharField(max_length=180)),
                ("materia", models.CharField(max_length=180)),
                ("semestre", models.CharField(max_length=180)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Calificacion",
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
                ("alumno", models.CharField(max_length=180)),
                ("parcial", models.CharField(max_length=180)),
                ("actividad", models.CharField(max_length=180)),
                ("observacion", models.CharField(max_length=180)),
                ("calificacion", models.DecimalField(decimal_places=2, max_digits=5)),
                ("fecha", models.DateTimeField(auto_now_add=True)),
                (
                    "materia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="todo_api.materia",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
