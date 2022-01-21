from django.contrib import admin
from .models import *

class TableUsuario(admin.ModelAdmin):
    list_display= ('id','nombres','email', 'password')

class TableBodega(admin.ModelAdmin):
    list_display= ('id', 'nombre', 'direccion')    

class TableProducto(admin.ModelAdmin):
    list_display= ('id', 'codigo', 'nombre','detalle','valor')   

class TableBodegaProducto(admin.ModelAdmin):
    list_display= ('id', 'idBodega', 'idProducto','stock')    


admin.site.register(usuario,TableUsuario)
admin.site.register(bodega,TableBodega)
admin.site.register(producto,TableProducto)
admin.site.register(bodegaProducto,TableBodegaProducto)