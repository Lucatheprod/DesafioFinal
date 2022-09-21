from django.urls import path
from AppThatBeer.views import crearCliente, crearDistribuidor, crearPatrocinador, crearProducto, clientes, \
    distribuidores, patrocinadores, inicio, aboutus, noticias, buscarProducto, \
    leerProducto, eliminarProducto, editarProducto, buscarPatrocinador, buscarDistribuidor, \
    buscarCliente, crearNoticia, leerNoticia



urlpatterns = [
    # url generales
    path('', inicio, name= 'AppThatBeerInicio'),
    path('sobrenosotros/', aboutus, name= 'AppThatBeerAboutUs'),
    

    # url productos
    path('productos/', leerProducto, name='AppThatBeerLeerProductos'),
    path('productos/crear', crearProducto, name='AppThatBeerCrearProducto'),
    path('productos/buscar', buscarProducto, name='AppThatBeerBuscarProducto'),
    path('productos/eliminar/<str:codigo>', eliminarProducto, name='AppThatBeerEliminarProducto'),
    path('productos/editar/<str:codigo>', editarProducto, name='AppThatBeerEditarProducto'),

    # url distribuidores
    path('distribuidores/', distribuidores, name='AppThatBeerDistribuidores'),
    path('distribuidores/crear', crearDistribuidor, name='AppThatBeerCrearDistribuidor'),
    path('distribuidores/buscar', buscarDistribuidor, name='AppThatBeerBuscarDistribuidor'),

    # url patrocinadores
    path('patrocinadores/', patrocinadores, name='AppThatBeerPatrocinadores'),
    path('patrocinadores/crear', crearPatrocinador, name='AppThatBeerCrearPatrocinador'),
    path('patrocinadores/buscar', buscarPatrocinador, name='AppThatBeerBuscarPatrocinador'),

    # url clientes
    path('clientes/', clientes, name='AppThatBeerClientes'),
    path('clientes/crear', crearCliente, name='AppThatBeerCrearCliente'),
    path('clientes/buscar', buscarCliente, name='AppThatBeerBuscarCliente'),

    # url noticias
    path('noticias/', noticias, name='AppThatBeerNoticias'),
    path('noticias/crear', crearNoticia, name='AppThatBeerCrearNoticia'),
    path('noticias/leer/<str:titulo>', leerNoticia, name='AppThatBeerLeerNoticia'),

]
