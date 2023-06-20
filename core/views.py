from django.shortcuts import render
from django.urls import reverse_lazy
# user
from django.contrib.auth.models import User
# generics 

from django.views.generic import CreateView

# models

from .models import *

# forms

from .form import  *

# Create your views here.

def login(request):
    
    form = iniciarSesion
    
    return render(request, 'login.html', {'form':form})

def home(request):
    
    return render(request, 'index.html')

def registro(request):
    
    return render(request, 'registro.html')

def transferencia(request):
    
    return render(request, 'transferencia.html')

def donaciones(request):
    
    return render(request, 'Donaciones.html')


def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            nivelEducacional = request.POST.get("nivelEducacional")
            region = request.POST.get("region")
            Cliente.objects.update_or_create(user=user, region=region, nivelEducacional=nivelEducacional )
            return render(request, 'index.html')
    form = RegistroForm()
    return render(request, "registro.html", {'form': form})

