from rest_framework import serializers
from .models import *


# Producto
class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Producto
        fields = '__all__'
        
class DonacionesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Donaciones
        fields = '__all__'
        
class PagarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Pagar
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Carrito
        fields = '__all__'
        
        
class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = '__all__'