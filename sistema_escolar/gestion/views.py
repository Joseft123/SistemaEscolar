from django.shortcuts import render, redirect
from .forms import CalificarForm

def registrar_calificacion(request):
    if request.method == 'POST':
        form = CalificarForm(request.POST)
        if form.is_valid():
            # Aquí guardarías la nota en un modelo "Calificacion" 
            # (que deberías crear en models.py)
            print(f"Estudiante: {form.cleaned_data['estudiante']}")
            print(f"Nota: {form.cleaned_data['nota']}")
            return redirect('exito') # Redirige tras guardar
    else:
        form = CalificarForm()
    
    return render(request, 'gestion/calificar.html', {'form': form})