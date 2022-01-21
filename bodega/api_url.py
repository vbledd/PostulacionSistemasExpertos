from django.urls import path
from . import models
from . import api_views as api

app_name = 'api'
urlpatterns = [

   #PRODUCTOS
   #GET RESUMEN BODEGAS
   path("productos/resumen", api.resumenProductos.as_view(), name="productos-resumen"),
   #GET listar todos los productos / sin parametros
   path("productos/listar", api.productosListar.as_view(), name="productos-listar"),
   #GET buscador de productos / buscar
   path("productos/buscador", api.productosBuscador.as_view(), name="productos-buscar"),
   #GET obtener datos de 1 producto / id
   path("productos/datos", api.productosDatos.as_view(), name="productos-datos"),
   #POST crear un producto/ codigo,nombre,detalle,valor
   path("productos/crear", api.productosCrear.as_view(), name="productos-crear"),
   #POST editar un producto / codigo,nombre,detalle,valor
   path("productos/editar", api.productosEditar.as_view(), name="productos-editar"),
   #POST eliminar un producto / id
   path("productos/eliminar", api.productosEliminar.as_view(), name="productos-eliminar"),

   #BODEGAS
   #GET RESUMEN BODEGAS
   path("bodegas/resumen", api.resumenBodegas.as_view(), name="bodegas-resumen"),
   #GET listar todas las bodegas
   path("bodegas/listar", api.bodegasListar.as_view(), name="bodegas-listar"),
   #GET obtener datos de 1 bodega / id
   path("bodegas/datos", api.bodegaDatos.as_view(), name="bodegas-datos"),
   #POST crear bodega / nombre, direccion
   path("bodegas/crear", api.bodegasCrear.as_view(), name="bodegas-crear"),
   #POST editar bodega / nombre, direccion
   path("bodegas/editar", api.bodegasEditar.as_view(), name="bodegas-editar"),
   #POST eliminar bodega / id
   path("bodegas/eliminar", api.bodegasEliminar.as_view(), name="bodegas-eliminar"),

   #PRODUCTOS EN BODEGAS
   #GET lista todos los productos de todas las bodegas / sin parametros
   path("bodegas/productos/listar", api.bodegasProductosListar.as_view(), name="bodegas-productos-listar"),
   #GET lista los productos en una bodega en especifico / idBodega
   path("bodegas/productos", api.bodegasListarProductos.as_view(), name="bodegas-productos"),
   #GET buscar producto especifico de una bodega / idBodega idProducto
   path("bodegas/productos/especifico", api.BodegaProductoEspecifico.as_view(), name="bodegas-productos-especifico"),
   #POST agregar stock en una bodega / idBodega,idProducto,stock
   path("bodegas/stock/agregar", api.AgregarStock.as_view(), name="bodegas-stock-agregar"),
   

]