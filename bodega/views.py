from re import U
from django.shortcuts import render
from .login import *
from .models import *
from django.contrib.auth.hashers import make_password, check_password



@requiereLogin
def index(request):

    return render(request, 'paginas/index.html')


def loginForm(request):
    try:
        if request.session['login']:
            return redirect('index')
    except:
        return render(request, 'login.html')

def login(request):
    usuarioEmail = request.POST.get('email')
    password = request.POST.get('pass')

    print(f"{usuarioEmail}, {password}")
    
    try: 
        registro = usuario.objects.get(email = usuarioEmail)
        print(registro.password)
        print(check_password(password,registro.password))

        if check_password(password,str(registro.password)):
           
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

    del request.session['login']
    return redirect('login-formulario')

@requiereLogin
def productos(request):
    return render(request, 'paginas/productos.html')

@requiereLogin
def bodegas(request):
    return render(request, 'paginas/bodegas.html')

@requiereLogin
def ingresoStock(request):
    return render(request, 'paginas/ingresoStock.html')

@requiereLogin
def bodegasProductos(request):
    id = request.GET.get('id')
    registro = bodega.objects.get(id=id)
    return render(request, 'paginas/bodegasProductos.html',{'bodega' : registro})