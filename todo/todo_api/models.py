from django.db import models
from django.contrib.auth.models import User



class Todo(models.Model):
    task = models.CharField(max_length=180)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    completed = models.BooleanField(default=False,blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.task
    



    
class Materia(models.Model):
    claveMateria = models.CharField(max_length=180)
    materia = models.CharField(max_length=180)
    semestre = models.CharField(max_length=180)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.id
    
    
class Calificacion(models.Model):
    alumno = models.CharField(max_length=180)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    parcial = models.CharField(max_length=180)
    actividad = models.CharField(max_length=180)
    observacion = models.CharField(max_length=180)
    calificacion = models.DecimalField(max_digits=5,decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.id


# Create your models here.
