# gestion/admin.py
from django.contrib import admin
from .models import Profesor, Estudiante, Curso, Calificacion # Asegúrate de incluir Calificacion

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Calificacion) # Agrega esta línea