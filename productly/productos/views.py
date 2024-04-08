from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import ProductoForm
from .models import Producto

# Create your views here.

# /productos


def index(request):
    productos = Producto.objects.all()  # Todos los registros de DDBB
    return render(
        request,
        'index.html',  # La plantilla
        context={'productos': productos}  # Los datos en forma de diccionario
    )


def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    return render(
        request,
        'detalle.html',
        context={'producto': producto}
    )

    # try:
    #     producto = Producto.objects.get(id=producto_id)

    #     return render(
    #         request,
    #         'detalle.html',
    #         context={'producto': producto}
    #     )
    # except Producto.DoesNotExist:
    #     raise Http404()


def formulario(request):
    # Validando que es POST
    if request.method == 'POST':
        # Le pasamos todo lo que viene dentro de la petición POST
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar en DDBB
            # Redirigirnos a la lista de productos
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()

    # Si algo falló, regresamos a la misma pg
    # Además, los errores estarán en la variable form y serán visibles
    return render(
        request,
        'producto_form.html',
        {'form': form}
    )
