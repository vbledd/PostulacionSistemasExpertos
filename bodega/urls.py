from django.urls import include, path
from . import views
from django.contrib import admin


urlpatterns = [
    #Rutas de administracion Django
    path('admin/', admin.site.urls),
    #Rutas de API REST
    path('api/', include('bodega.api_url')),
    #Rutas Login
    path("login/", views.login, name="login"),
    path("login/formulario", views.loginForm, name="login-formulario"),
    path("logout", views.logout, name="Logout"),
    #Paginas
    path("",views.index, name="index"),
    path("productos",views.productos, name="productos"),
    path("bodegas",views.bodegas, name="bodegas"),
    path("bodegas/ingreso-stock",views.ingresoStock, name="bodegas-ingreso-stock"),
    path("bodegas/productos",views.bodegasProductos, name="bodegas-productos"),
]

    
    