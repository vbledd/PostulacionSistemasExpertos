from re import U
from django.shortcuts import render
from .login import *
from .models import *
from django.contrib.auth.hashers import make_password, check_password



@requiereLogin
def index(request):
    #renderiza el html 
    return render(request, 'paginas/index.html')


def loginForm(request):
    # utilizamos uun try para controlar excepciones
    try:
        #si el usuario tiene iniciada la sesion se redirecciona
        #al index, de no ser asi renderiza el html que contiene el login
        if request.session['login']:
            return redirect('index')
    except:
        return render(request, 'login.html')

def login(request):
    #guardamos en variables los parametros post del request
    usuarioEmail = request.POST.get('email')
    password = request.POST.get('pass')

    
    try: 
        #buscamos en la bd si existe un usuario con el email ingresado
        #en caso de no existir nos mostrara un mensaje de error a traves del except
        registro = usuario.objects.get(email = usuarioEmail)
        #comprobamos la contraseña ingresada con el hash de la contraseña en la bd
        if check_password(password,str(registro.password)):
           #si esta todo ok guardamos los datos del usuario en la session
            datos = {
                'id' : registro.id,
                'email' : registro.email,
                'nombres' : registro.nombres
               
            }
            request.session['login'] = datos
            return redirect('index')
        else:
            return ventanaError(request, 224)
    except Exception as e:
        print(e)
        return ventanaError(request, 224)

@requiereLogin
def logout(request):
    #eliminamos la sesion del usuario
    del request.session['login']
    return redirect('login-formulario')

@requiereLogin
def productos(request):
    #renderiza el html de productos
    return render(request, 'paginas/productos.html')

@requiereLogin
def bodegas(request):
    #renderiza el html de bodegas
    return render(request, 'paginas/bodegas.html')

@requiereLogin
def ingresoStock(request):
    #renderiza el html de ingreso de stock
    return render(request, 'paginas/ingresoStock.html')

@requiereLogin
def bodegasProductos(request):
    #renderiza el html quue contiene las bodegas
    id = request.GET.get('id')
    registro = bodega.objects.get(id=id)
    return render(request, 'paginas/bodegasProductos.html',{'bodega' : registro})