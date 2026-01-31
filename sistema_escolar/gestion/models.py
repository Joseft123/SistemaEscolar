from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.get_full_name()

class Estudiante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.usuario.last_name

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)
    estudiantes = models.ManyToManyField(Estudiante)

    def __str__(self):
        return self.nombre