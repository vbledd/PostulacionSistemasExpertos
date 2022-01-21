from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

def ventanaError(request, code):
    
    codigos = [
        {
            'code' : 224,
            'titulo' : 'Error de Login',
            'descripcion' : 'Email o contraseña erroneos'
        },
        {
            'code' : 333,
            'titulo' : 'Error Desconocido',
            'descripcion' : 'Error no identificado'
        },
        {
            'code' : 555,
            'titulo' : 'Sin Permiso',
            'descripcion' : 'No tienes permisos para entrar en esta sección'
        },
    ]


    for item in codigos:
        

        if item['code'] == code:
            
            
            return render(request,'error.html',{'mensaje': item})

    nones ={
            'code' : 999,
            'titulo' : 'Error Desconocido',
            'descripcion' : 'Error no identificado'
        }

    return render(request,'error.html',{'mensaje': nones})
  

    