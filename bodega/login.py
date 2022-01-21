from django.core.exceptions import PermissionDenied
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .errores import *

def requiereLogin(function):

    def comprobar(request, *callback_args, **callback_kwargs):
       
        try: 
            usuario = request.session['login']
            print(usuario)
            if usuario != '':
               return function(request, *callback_args, **callback_kwargs)
            else:
                return redirect('login-formulario')


        
        except Exception as e:
            print(e)
            #si el usuario no esta logeado pasa esto
            return redirect('login-formulario')
            
        


    return comprobar