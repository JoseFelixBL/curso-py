from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.

# /productos


def index(request):
    #    return HttpResponse('¡Hola Mundo!') # para ver que llegamos a esta pg.

    # Para hacer un prototyping rápido devuelvo una lista de JSON
    # productos = Producto.objects.filter(puntaje=5)
    # productos = Producto.objects.filter(puntaje__gte=3) # __lte, __gt, __lt
    # productos = Producto.objects.get(pk=1) # solo el que tenga primary key = 1

    productos = Producto.objects.all().values()  # Todos los registros de DDBB
    print(productos)
    # return HttpResponse(productos[0].nombre)
    return JsonResponse(list(productos), safe=False)
