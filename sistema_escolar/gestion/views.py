from django.shortcuts import render, redirect
from .forms import CalificarForm
from .models import Calificacion # Importamos el nuevo modelo

def registrar_calificacion(request):
    if request.method == 'POST':
        form = CalificarForm(request.POST)
        if form.is_valid():
            # Creamos el registro en la base de datos
            Calificacion.objects.create(
                estudiante=form.cleaned_data['estudiante'],
                nota=form.cleaned_data['nota'],
                comentario=form.cleaned_data['comentario']
            )
            return render(request, 'gestion/calificar.html', {
                'form': CalificarForm(), # Limpia el formulario
                'mensaje': '¡Calificación guardada con éxito!' 
            })
    else:
        form = CalificarForm()
    
    return render(request, 'gestion/calificar.html', {'form': form})