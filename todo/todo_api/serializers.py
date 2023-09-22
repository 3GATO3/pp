from rest_framework import serializers
from .models import Todo
from .models import Calificacion

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["task","completed","timestamp", "updated", "user"]

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = ["id","alumno ","materia","parcial","actividad","observacion","calificacion","fecha"]
