from locale import resetlocale
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core import serializers
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Sum

#creamos una funcion que nos permite formatear los datos de la bd a JSON
def FormatoJson(consulta):
    respuesta = serializers.serialize("json", consulta, use_natural_foreign_keys=True)
    
    return respuesta

#esta vista nos retorna todos los productos existentes en la bd
class productosListar(APIView):

    def get(self, request, format=None):
        try:
            registro = producto.objects.all()
            data = FormatoJson(registro)
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

#esta vista nos retorna los productos a traves de un parametro de busqueda y de esta forma filtra los
#datos segun el nombre ingresado en el parametro 'buscar'
class productosBuscador(APIView):

    def get(self, request, format=None):
        try:
            registro = producto.objects.filter(nombre__icontains=request.GET.get('buscar'))
            data = FormatoJson(registro)
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

#esta vista nos retorna los datos de un producto en particular el cual es filtrado a traves de su id
class productosDatos(APIView):

    def get(self, request, format=None):
        try:
            registro = producto.objects.filter(id=request.GET.get('id'))
            data = FormatoJson(registro)
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


#se reciben los parametros codigo,nombre,detalle,valor para crear el producto en la bd
class productosCrear(APIView):

    def post(self, request, format=None):
        try:
            if producto.objects.filter(codigo=request.POST.get('codigo')).exists():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                registro = producto()
                registro.codigo = request.POST.get('codigo')
                registro.nombre = request.POST.get('nombre')
                registro.detalle = request.POST.get('detalle')
                registro.valor = request.POST.get('valor')
                registro.save()

                return Response(status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

#se reciben los parametros id,codigo,nombre,detalle,valor para modificar el producto en la bd
#ademas de comprobar que no exista un codigo duplicado
class productosEditar(APIView):

    def post(self, request, format=None):
        try:
            registro = producto.objects.get(id=request.POST.get('id'))
            if registro.codigo != request.POST.get('codigo'):

                if producto.objects.filter(codigo=request.POST.get('codigo')).exists() == False:
                    registro.codigo = request.POST.get('codigo')
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)

            registro.nombre = request.POST.get('nombre')
            registro.detalle = request.POST.get('detalle')
            registro.valor = request.POST.get('valor')
            registro.save()
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

#recibe por parametro el id del producto para eliminarlo de la bd
class productosEliminar(APIView):

    def post(self, request, format=None):
        try:
            registro = producto.objects.get(id=request.POST.get('id'))
            registro.delete()
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

#lista todas las bodegas existentes en la bd
class bodegasListar(APIView):

    def get(self, request, format=None):
        try:
            registro = bodega.objects.all()
            data = FormatoJson(registro)
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

#muestra los datos especificos de una bodega a traves de su id
class bodegaDatos(APIView):

    def get(self, request, format=None):
        try:
            registro = bodega.objects.filter(id=request.GET.get('id'))
            data = FormatoJson(registro)
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

#se reciben los parametros nombre,direccion para crear una bodega en la bd
#ademas de comprobar si el nombre esta duplicado
class bodegasCrear(APIView):

    def post(self, request, format=None):
        try:
            if bodega.objects.filter(nombre=request.POST.get('nombre')).exists() == False:
                registro = bodega()
                registro.nombre = request.POST.get('nombre')
                registro.direccion = request.POST.get('direccion')
                registro.save()

                return Response(status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

#se reciben los parametros nombre, direccion para editar la informacion en la bd y comprueba los nombres duplicados
class bodegasEditar(APIView):

    def post(self, request, format=None):
        try:
            registro = bodega.objects.get(id=request.POST.get('id'))

            if registro.nombre != request.POST.get('nombre'):

                    if bodega.objects.filter(nombre=request.POST.get('nombre')).exists() == False:
                        registro.nombre = request.POST.get('nombre')
                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                    
            registro.direccion = request.POST.get('direccion')
            registro.save()

            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

#se recibe el id para eliminar una bodega de la bd
class bodegasEliminar(APIView):

    def post(self, request, format=None):
        try:
            registro = bodega.objects.get(id=request.POST.get('id'))
            registro.delete()

            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

#lista los productos que contienen todas las bodegas
class bodegasProductosListar(APIView):

    def get(self, request, format=None):
        try:
            registro = bodegaProducto.object.all()
            data = FormatoJson(registro)

            return Response(data,status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

#lista los productos de una bodega en especifico a traves de la id de la bodega
class bodegasListarProductos(APIView):

    def get(self, request, format=None):
        try:
           
            registro = bodegaProducto.objects.filter(idBodega=request.GET.get('idBodega'))
            data = FormatoJson(registro)

            return Response(data,status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

#modifica el stock de un producto obteniendo el id de la bodega y el id del producto
#para modificar o agregar stock al producto,esto comprueba si existe un producto en la bodega
#si este existe modifica el stock, de no existir agrega el producto a la bodega con el stock enviado
class AgregarStock(APIView):

    def post(self, request, format=None):
        try:
            IDBodega = request.POST.get('idBodega')
            IDProducto = request.POST.get('idProducto')
            ValorStock = int(request.POST.get('stock'))

            if bodegaProducto.objects.filter(idBodega=IDBodega,idProducto=IDProducto).exists():
                registro = bodegaProducto.objects.get(idBodega=IDBodega,idProducto=IDProducto)
                if ValorStock <= 0:
                    registro.delete()
                else:
                    registro.stock = ValorStock
                    registro.save()
            else:
                registro = bodegaProducto()
                registro.idBodega = bodega.objects.get(id=IDBodega)
                registro.idProducto = producto.objects.get(id=IDProducto)
                if ValorStock <= 0:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    registro.stock = ValorStock
                    registro.save()
  
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

#nos muestra los datos de un producto especifico de una bodega recibiendo el id de la bodega y el id del producto
class BodegaProductoEspecifico(APIView):

    def get(self, request, format=None):
        try:
            IDBodega = request.GET.get('idBodega')
            IDProducto = request.GET.get('idProducto')
           
            if bodegaProducto.objects.filter(idBodega=IDBodega,idProducto=IDProducto).exists():
                datos = bodegaProducto.objects.filter(idBodega=IDBodega,idProducto=IDProducto)
                datos = FormatoJson(datos)
                return Response(datos,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)


        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)



#nos lista los ultimos 10 productos ingresados
class resumenProductos(APIView):

    def get(self, request, format=None):
        try:
            cantidad = producto.objects.all().count()
            registroProductos = producto.objects.all()[0:10]
            registroProductos = FormatoJson(registroProductos)
            data = {'cantidad':cantidad, 'datos': registroProductos}
            return Response(data,status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
#nos devuelve datos sobre la cantidad de productos ingresados en cada bodega y el stock total sumado de
#todas las bodegas
class resumenBodegas(APIView):

    def get(self, request, format=None):
        try:
            regBodegas = bodega.objects.all()
            total = bodegaProducto.objects.all().aggregate(Sum('stock'))
            
            datos = []

            for items in regBodegas:
                reg = bodegaProducto.objects.filter(idBodega = items.id).count()
                a = {'id':items.id, 'nombre': items.nombre, 'cantidad':reg}
                datos.append(a)

            data = [{'total':total['stock__sum'], 'datos':datos}]

            return Response(data,status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)