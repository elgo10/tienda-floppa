from django.shortcuts import redirect, render
from django.urls import reverse_lazy
# user
from django.contrib.auth.models import User
# generics 

from django.views.generic import CreateView, ListView

# models

from .models import *


# Login required
from django.contrib.auth.decorators import login_required


# forms

from .form import  *


# API REST FRAMEWORK
from .serializers import *
# GENERICS API
from rest_framework import generics


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

def producto_delete(request, pk):
    
    prod_carrito = Carrito.objects.get(id = pk)
    
    if request.method == "POST":
        
        prod_carrito.delete()
        
        return redirect('carrito')
    
    return render(request, 'delete_carrito.html', {'prod_carrito': prod_carrito})

class CreateProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'registrar_producto.html'
    success_url = reverse_lazy('home')

@login_required(login_url='login')
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


def list_productos(request):
    
    productos = Producto.objects.all()
    
    return render(request, 'list_productos.html', {'productos': productos})

def delete_producto(request, pk):
    
    productos = Producto.objects.get(id=pk)
    
    return render(request, 'delete_producto.html', {'productos': productos})

# __________________ API VIEWS ______________

# Producto
class ApiPRoducts(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class ApiProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'

# Carrito

class ApiCarritos(generics.ListCreateAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    
class ApiCarrito(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'

# Donaciones

class ApiDonaciones(generics.ListCreateAPIView):
    queryset = Donaciones.objects.all()
    serializer_class = DonacionesSerializer
    
class ApiDonacion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donaciones.objects.all()
    serializer_class = DonacionesSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
# Pagar

class ApiPagos(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class ApiPago(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
 

# Cliente   
class ApiClientes(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class ApiCliente(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    