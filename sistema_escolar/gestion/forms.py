from django import forms
from .models import Estudiante, Curso

class CalificarForm(forms.Form):
    # Desplegable con los estudiantes
    estudiante = forms.ModelChoiceField(queryset=Estudiante.objects.all())
    # Campo numérico para la nota
    nota = forms.DecimalField(max_digits=4, decimal_places=2, min_value=0, max_value=10)
    comentario = forms.CharField(widget=forms.Textarea, required=False)