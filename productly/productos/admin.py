from django.contrib import admin
from .models import Categoria, Producto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


class ProductoAdmin(admin.ModelAdmin):
    # fields = para indicar los campos que queremos que aparez<can en el formulario
    exclude = ('creado_en',)
    list_display = ('id', 'nombre', 'stock', 'creado_en')


# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
