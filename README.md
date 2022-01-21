# PostulacionSistemasExpertos
Miguel Salinas Nicoletti

url en servidor con la aplicación en funcionamiento: http://186.20.207.79:8888/

datos de acceso para login <br/>
email: admin@admin.cl <br/>
pass: admin <br/>

Para la confección de este sistema se utilizo DJANGO implementando una API REST a traves de la libreria djangorestframework
basicamente la api se encarga del funcionamiento y la logica para crear,editar,eliminar,listar datos de la base de datos. mientras
que se consume con javascript vue utilizando axios para los request.

tome la desición de realizarlo de esta forma puesto que nos permite ahorrar tiempos de carga al no tener que recargar la pagina una y otra vez
para mostrar cambios en esta, de esta forma ahorrando recursos y maximizando el uso del servidor. ademas de tener la gran ventaja de llamar datos
a traves de cualquier aplicación realizada en otro tipo de lenguaje, esto nos permite realizar una aplicación escalable sin necesidad de modificar
todo el codigo fuente.

el archivo encargado de realizar toda la logica con la bd y mostrar a traves de la api es: api_views.py
dentro de este he dejado un comentario sobre que hace cada parte.

las rutas para consultar la api son las siguientes: <br/>

#PRODUCTOS <br/>
   #GET RESUMEN BODEGAS <br/>
   api/productos/resumen <br/>
   #GET listar todos los productos / sin parametros <br/>
   api/productos/listar <br/>
   #GET buscador de productos / buscar <br/>
   api/productos/buscador <br/>
   #GET obtener datos de 1 producto / id <br/>
   api/productos/datos <br/>
   #POST crear un producto/ codigo,nombre,detalle,valor <br/>
   api/productos/crear <br/>
   #POST editar un producto / codigo,nombre,detalle,valor <br/>
   api/productos/editar <br/>
   #POST eliminar un producto / id <br/>
   api/productos/eliminar <br/>

   #BODEGAS <br/>
   #GET RESUMEN BODEGAS <br/>
   api/bodegas/resumen <br/>
   #GET listar todas las bodegas <br/>
   api/bodegas/listar <br/>
   #GET obtener datos de 1 bodega / id <br/>
   api/bodegas/datos <br/>
   #POST crear bodega / nombre, direccion <br/>
   api/bodegas/crear <br/>
   #POST editar bodega / nombre, direccion <br/>
   api/bodegas/editar <br/>
   #POST eliminar bodega / id <br/>
   api/bodegas/eliminar <br/>

   #PRODUCTOS EN BODEGAS <br/>
   #GET lista todos los productos de todas las bodegas / sin parametros <br/>
   api/bodegas/productos/listar <br/>
   #GET lista los productos en una bodega en especifico / idBodega <br/>
   api/bodegas/productos <br/>
   #GET buscar producto especifico de una bodega / idBodega idProducto <br/>
   api/bodegas/productos/especifico <br/>
   #POST agregar stock en una bodega / idBodega,idProducto,stock <br/>
   api/bodegas/stock/agregar <br/>
