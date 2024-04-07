from django.urls import path
from . import views

app_name = 'productos'
urlpatterns = [
    path('', views.index, name='index'),
    path('formulario', views.formulario, name='formulario'),
    path(
        '<int:producto_id>',  # parámetro
        views.detalle,  # Función detalle en views
        # name='producto_detalle'  # Nombre de la ruta, PONERLO SIEMPRE
        name='detalle'  # Nombre de la ruta, PONERLO SIEMPRE
    ),
]
