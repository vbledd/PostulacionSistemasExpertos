# PostulacionSistemasExpertos
Miguel Salinas Nicoletti

url en servidor con la aplicación en funcionamiento: http://186.20.207.79:8888/

datos de acceso para login
email: admin@admin.cl
pass: admin

Para la confección de este sistema se utilizo DJANGO implementando una API REST a traves de la libreria djangorestframework
basicamente la api se encarga del funcionamiento y la logica para crear,editar,eliminar,listar datos de la base de datos. mientras
que se consume con javascript vue utilizando axios para los request.

tome la desición de realizarlo de esta forma puesto que nos permite ahorrar tiempos de carga al no tener que recargar la pagina una y otra vez
para mostrar cambios en esta, de esta forma ahorrando recursos y maximizando el uso del servidor. ademas de tener la gran ventaja de llamar datos
a traves de cualquier aplicación realizada en otro tipo de lenguaje, esto nos permite realizar una aplicación escalable sin necesidad de modificar
todo el codigo fuente.

el archivo encargado de realizar toda la logica con la bd y mostrar a traves de la api es: api_views.py
dentro de este he dejado un comentario sobre que hace cada parte.

las rutas para consultar la api son las siguientes:

#PRODUCTOS
   #GET RESUMEN BODEGAS
   api/productos/resumen
   #GET listar todos los productos / sin parametros
   api/productos/listar
   #GET buscador de productos / buscar
   api/productos/buscador
   #GET obtener datos de 1 producto / id
   api/productos/datos"
   #POST crear un producto/ codigo,nombre,detalle,valor
   api/productos/crear
   #POST editar un producto / codigo,nombre,detalle,valor
   api/productos/editar
   #POST eliminar un producto / id
   api/productos/eliminar

   #BODEGAS
   #GET RESUMEN BODEGAS
   api/bodegas/resumen
   #GET listar todas las bodegas
   api/bodegas/listar
   #GET obtener datos de 1 bodega / id
   api/bodegas/datos
   #POST crear bodega / nombre, direccion
   api/bodegas/crear
   #POST editar bodega / nombre, direccion
   api/bodegas/editar
   #POST eliminar bodega / id
   api/bodegas/eliminar

   #PRODUCTOS EN BODEGAS
   #GET lista todos los productos de todas las bodegas / sin parametros
   api/bodegas/productos/listar
   #GET lista los productos en una bodega en especifico / idBodega
   api/bodegas/productos
   #GET buscar producto especifico de una bodega / idBodega idProducto
   api/bodegas/productos/especifico
   #POST agregar stock en una bodega / idBodega,idProducto,stock
   api/bodegas/stock/agregar
