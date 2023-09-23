from rest_framework import serializers
from django.contrib.auth.models import User, Group

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

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


