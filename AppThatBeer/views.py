import datetime
from urllib import request
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Template, Context
from AppThatBeer.models import Cliente, Noticia, Producto, Distribuidor, Patrocinador
from AppThatBeer.forms import ProductoFormulario, ClienteFormulario, DistribuidorFormulario, PatrocinadorFormulario, \
    NoticiaFormulario


# vista de inicio
def inicio (request):
    return render(request, 'index.html')


# vista de productos
def leerProducto(request):
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request, 'AppThatBeer/producto/leer.html', contexto)


# vista de distribuidores
def distribuidores(request):
    distribuidoreslistado = Distribuidor.objects.all()
    return render(request, 'AppThatBeer/distribuidor/distribuidores.html', {"distribuidores": distribuidoreslistado})


# vista de clientes
def clientes(request):
    clienteslistado = Cliente.objects.all()
    return render(request, 'AppThatBeer/cliente/clientes.html', {"clientes": clienteslistado})


# vista de patrocinadores
def patrocinadores (request):
    patrocinadoreslistado = Patrocinador.objects.all()
    return render(request, 'AppThatBeer/patrocinador/patrocinadores.html', {"patrocinadores": patrocinadoreslistado})


# vista de noticias o blog
def noticias (request):
    noticiaslistado = Noticia.objects.all()
    return render(request, 'AppThatBeer/noticias/generales.html', {"noticias": noticiaslistado})


# vista de sobre nosotros
def aboutus(request):
    return render(request, 'AppThatBeer/aboutus/aboutus.html')


# buscar producto
def buscarProducto(request):
    if request.GET['variedad']:
        variedad = request.GET['variedad']
        productos = Producto.objects.filter(variedad__contains=variedad)

        return render(request, 'AppThatBeer/producto/resultadobusqueda.html', {'productos': productos, 'variedad': variedad})
    else:
        return redirect('AppThatBeerLeerProductos')


# buscar distribuidor
def buscarDistribuidor(request):
    if request.GET['provincia']:
        provincia = request.GET['provincia']
        distribuidores = Distribuidor.objects.filter(provincia__contains=provincia)

        return render(request, 'AppThatBeer/distribuidor/resultadobusqueda.html', {'distribuidores': distribuidores, 'provincia': provincia})
    else:
        return redirect('AppThatBeerDistribuidores')


# buscar cliente
def buscarCliente(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        clientes = Cliente.objects.filter(nombre__contains=nombre)

        return render(request, 'AppThatBeer/cliente/resultadobusqueda.html', {'clientes': clientes, 'nombre': nombre})
    else:
        return redirect('AppThatBeerClientes')


# buscar patrocinador
def buscarPatrocinador(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        patrocinadores = Patrocinador.objects.filter(nombre__contains=nombre)

        return render(request, 'AppThatBeer/patrocinador/resultadobusqueda.html', {'patrocinadores': patrocinadores, 'nombre': nombre})
    else:
        return redirect('AppThatBeerPatrocinadores')



def leerNoticia(request, titulo):
    noticia = Noticia.objects.get(titulo=titulo)
    return render(request, 'AppThatBeer/noticias/publicacion.html', {"noticia": noticia})



# crear producto
@login_required
def crearProducto(request):
    if request.method == 'POST':
        mi_formulario = ProductoFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre = informacion['nombre']
            variedad = informacion['variedad']
            contenido_ml = informacion['contenido_ml']
            codigo = informacion['codigo']
            descripcion = informacion['descripcion']

            producto = Producto(nombre=nombre, variedad=variedad, contenido_ml=contenido_ml, codigo=codigo,
                                descripcion=descripcion)
            producto.save()

            return redirect('AppThatBeerLeerProductos')
        else:
            return redirect('AppThatBeerInicio')
    contexto = {
        'producto_form': ProductoFormulario()
    }
    return render(request, 'AppThatBeer/producto/crear.html', contexto)


# crear cliente
@login_required
def crearCliente(request):
    if request.method == 'POST':
        mi_formulario = ClienteFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre = informacion['nombre']
            apellido = informacion['apellido']
            email = informacion['email']
            direccion = informacion['direccion']
            provincia = informacion['provincia']
            cp = informacion['cp']
            dni = informacion['dni']

            cliente = Cliente(nombre=nombre, apellido=apellido, email=email, direccion=direccion, provincia=provincia, cp=cp, dni=dni)
            cliente.save()

            return redirect('AppThatBeerClientes')
    else:
        mi_formulario = ClienteFormulario()
    return render(request, 'AppThatBeer/cliente/crear.html', {'mi_formulario':mi_formulario})


# crear distribuidor
@login_required
def crearDistribuidor(request):
    if request.method == 'POST':
        mi_formulario = DistribuidorFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre = informacion['nombre']
            cuit = informacion['cuit']
            direccion = informacion['direccion']
            provincia = informacion['provincia']
            descuento = informacion['descuento']
            web = informacion['web']

            distribuidor = Distribuidor(nombre=nombre, cuit=cuit, direccion=direccion, provincia=provincia, descuento=descuento, web=web)
            distribuidor.save()

            return redirect('AppThatBeerDistribuidores')
    else:
        mi_formulario = DistribuidorFormulario()
    return render(request, 'AppThatBeer/distribuidor/crear.html', {'mi_formulario':mi_formulario})


# crear patrocinador
@login_required
def crearPatrocinador(request):
    if request.method == 'POST':
        mi_formulario = PatrocinadorFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nombre = informacion['nombre']
            rubro = informacion['rubro']
            slogan = informacion['slogan']
            antiguedad_anios = informacion['antiguedad_anios']
            web = informacion['web']

            patrocinador = Patrocinador(nombre=nombre, rubro=rubro, slogan=slogan, antiguedad_anios=antiguedad_anios, web=web)
            patrocinador.save()

            return redirect('AppThatBeerPatrocinadores')
    else:
        mi_formulario = PatrocinadorFormulario()
    return render(request, 'AppThatBeer/patrocinador/crear.html', {'mi_formulario': mi_formulario})


# crear noticia
@login_required
def crearNoticia(request):
    if request.method == 'POST':
        mi_formulario = NoticiaFormulario(request.POST, request.FILES)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            titulo = informacion['titulo']
            subtitulo = informacion['subtitulo']
            cuerpo = informacion['cuerpo']
            autor = informacion['autor']
            imagen = informacion['imagen']
            fecha_posteo = informacion['fecha_posteo']

            noticia = Noticia(
                titulo=titulo,
                subtitulo=subtitulo,
                cuerpo=cuerpo,
                autor=autor,
                imagen=imagen,
                fecha_posteo=fecha_posteo
            )
            noticia.save()
            messages.info(request,'Noticia creada con éxito')
            return redirect('AppThatBeerNoticias')
        else:
            messages.info(request, 'Algo salió mal... Inténtelo nuevamente')
            return redirect('AppThatBeerCrearNoticia')
    contexto = {
        'noticia_form': NoticiaFormulario()
    }
    return render(request, 'AppThatBeer/noticias/crear.html', contexto)


# eliminar producto
def eliminarProducto (request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect('AppThatBeerLeerProductos')


# editar producto
def editarProducto (request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto_form = ProductoFormulario(initial={
        'nombre':producto.nombre,
        'variedad':producto.variedad,
        'contenido_ml':producto.contenido_ml,
        'codigo':producto.codigo,
        'descripcion':producto.descripcion,
    })

    if request.method == 'POST':
        mi_form = ProductoFormulario(request.POST)

        if mi_form.is_valid():
            info = mi_form.cleaned_data
            producto.nombre = info['nombre']
            producto.variedad = info['variedad']
            producto.contenido_ml = info['contenido_ml']
            producto.codigo = info['codigo']
            producto.descripcion = info['descripcion']

            producto.save()
            return redirect('AppThatBeerLeerProductos')
    contexto = {
        'producto_form': producto_form,
    }
    return render(request, 'AppThatBeer/producto/editar.html', contexto)










