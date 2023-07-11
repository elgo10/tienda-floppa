from django.shortcuts import render
from django.urls import reverse_lazy
# user
from django.contrib.auth.models import User
# generics 

from django.views.generic import CreateView, ListView

# models

from .models import *

# forms

from .form import  *

# Create your views here.
# ___________ OPCIONES PRINCIPALES (NAVBAR U OTROS) ________________
def home(request):
    
    productos = Producto.objects.all()
    
    return render(request, 'index.html', {'producto': productos})

def registro(request):
    
    return render(request, 'registro.html')

def transferencia(request):
    
    return render(request, 'transferencia.html')

def donaciones(request):
    
    return render(request, 'Donaciones.html')

import pdb

def registroProducto(request):
    pdb.set_trace()
    if request.method == "POST":
        nombre  = request.POST.get("nombre")
        descripcion  = request.POST.get("descripcion")
        marca = request.POST.get("marca")
        cantidad  = request.POST.get("cantidad")
        precio  = request.POST.get("precio")
        img = request.POST.get("archive")
        Producto(nombre =  nombre, precio = precio, descripcion = descripcion, marca = marca, cantidad = cantidad, img = img ).save()
        
    return render(request, 'registrar_producto.html')

def carrito(request):
    
    user = request.user.id
    
    carrito = Carrito.objects.filter(user_id = user)
    
    total = 0
    for carritos in carrito:
        total += carritos.productos.precio
    
    return render(request, 'Carrito.html', {'carrito':carrito, 'total': total})

# Cambiar contraseña urls

def cambiarPassword(request):
    
    return render(request, 'cambiar_contraseña.html')

# Producto

def producto(request, pk):
    user = request.user
    producto = Producto.objects.get(id=pk)
    
    if user.is_authenticated:
        if request.method == "POST":
            
            Carrito(user = user, productos = producto).save()
            reverse_lazy('home')

    return render(request, 'productos.html', {'producto':producto})


# Pago

def pagar(request):
    
    user = request.user
    carrito = Carrito.objects.filter(user = user)
    
    if request.method == 'POST':
        nombre = request.POST.get("txtNombre")
        direccion =  request.POST.get("direccion")
        nro_depto  = request.POST.get("nro_depto")
        region = request.POST.get("region")
        comuna = request.POST.get("comuna")
        cod_postal = request.POST.get("cod_postal")
        # ____________ Tarjeta
        tarjeta_nom = request.POST.get("tarjeta_nom")
        nro_tarjeta = request.POST.get("nro_tarjeta")
        ccv = request.POST.get("ccv")
        fecha = request.POST.get("fecha")
        
        Pagar(nombre = nombre, direccion = direccion, nro_depto = nro_depto, region = region, comuna = comuna,
            cod_postal = cod_postal, tarjeta_nom = tarjeta_nom, nro_tarjeta = nro_tarjeta, ccv = ccv, fecha = fecha).save()
        
        carrito.delete()
        
        reverse_lazy("home")
    
    return render(request, '10pagar.html')

def debito(request):
    
    if request.method == "POST":
        nombre =  request.POST.get("nombre")
        nro_tarjeta = request.POST.get("nro_tarjeta")
        ccv = request.POST.get("ccv")
        fecha = request.POST.get("fecha")
        cantidad = request.POST.get("cantidad")
        
        Donaciones(nombre = nombre, nro_tarjeta = nro_tarjeta, fecha= fecha, ccv = ccv, cant= cantidad).save()
    
    return render(request, 'Debito.html')

def transferencia(request):
    
    return render(request, 'TRANSFERENCIA.html')

def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            nivelEducacional = request.POST.get("nivelEducacional")
            region = request.POST.get("region")
            rut = request.POST.get("rut")
            nombre = request.POST.get("nombre")
            apellido = request.POST.get("apellido")
            Cliente.objects.update_or_create(user=user, region=region, nivelEducacional=nivelEducacional, nombre=nombre, rut=rut, apellido=apellido, )
            return render(request, 'login.html')
    form = RegistroForm()
    return render(request, "registro.html", {'form': form})
