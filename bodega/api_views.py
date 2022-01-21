from locale import resetlocale
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core import serializers
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Sum


def FormatoJson(consulta):
    respuesta = serializers.serialize("json", consulta, use_natural_foreign_keys=True)
    
    return respuesta


class productosListar(APIView):

    def get(self, request, format=None):
        try:
            registro = producto.objects.all()
            data = FormatoJson(registro)
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class productosBuscador(APIView):

    def get(self, request, format=None):
        try:
            registro = producto.objects.filter(nombre__icontains=request.GET.get('buscar'))
            data = FormatoJson(registro)
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class productosDatos(APIView):

    def get(self, request, format=None):
        try:
            registro = producto.objects.filter(id=request.GET.get('id'))
            data = FormatoJson(registro)
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)



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

class productosEliminar(APIView):

    def post(self, request, format=None):
        try:
            registro = producto.objects.get(id=request.POST.get('id'))
            registro.delete()
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class bodegasListar(APIView):

    def get(self, request, format=None):
        try:
            registro = bodega.objects.all()
            data = FormatoJson(registro)
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class bodegaDatos(APIView):

    def get(self, request, format=None):
        try:
            registro = bodega.objects.filter(id=request.GET.get('id'))
            data = FormatoJson(registro)
            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

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

class bodegasEliminar(APIView):

    def post(self, request, format=None):
        try:
            registro = bodega.objects.get(id=request.POST.get('id'))
            registro.delete()

            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class bodegasProductosListar(APIView):

    def get(self, request, format=None):
        try:
            registro = bodegaProducto.object.all()
            data = FormatoJson(registro)

            return Response(data,status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class bodegasListarProductos(APIView):

    def get(self, request, format=None):
        try:
           
            registro = bodegaProducto.objects.filter(idBodega=request.GET.get('idBodega'))
            data = FormatoJson(registro)

            return Response(data,status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

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