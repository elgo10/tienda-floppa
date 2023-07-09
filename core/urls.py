from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('registro/', registrarse, name="registro"),
    path('transferencia/', transferencia),
    path('donaciones/', donaciones, name="donaciones"),
    path('carrito/', carrito, name="carrito"),
    path('registrarProducto/', registroProducto, name="registrarProd"),
    path('cambiarContraseña/', cambiarPassword, name="changePassword"),
    path('producto/<int:pk>', producto, name="producto"),
    path('pagar/', pagar, name="pagar"),
    path('debito/', debito, name="debito"),
    path('transferencia/', transferencia, name="transferir"),
]