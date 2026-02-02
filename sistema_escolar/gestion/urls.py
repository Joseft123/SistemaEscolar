from django.urls import path
from . import views

urlpatterns = [
    path('calificar/', views.registrar_calificacion, name='registrar_calificacion'),
]   