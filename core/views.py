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

def registroProducto(request):
    
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
    
    return render(request, '10pagar.html')

def debito(request):
    
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
            return render(request, 'index.html')
    form = RegistroForm()
    return render(request, "registro.html", {'form': form})

