from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('registro/', registrarse, name="registro"),
    path('transferencia/', transferencia),
    path('donaciones/', donaciones, name="donaciones"),
    path('carrito/', carrito, name="carrito"),
    path('delete/<int:pk>', producto_delete, name="carritoDelete"),
    path('registrarProducto/', CreateProducto.as_view(), name="registrarProd"),
    path('cambiarContraseña/', cambiarPassword, name="changePassword"),
    path('producto/<int:pk>', producto, name="producto"),
    path('pagar/', pagar, name="pagar"),
    path('debito/', debito, name="debito"),
    path('transferencia/', transferencia, name="transferir"),
    
    # CRUDS
    
    path('list_product/', list_productos, name="list_product"),
    path('delete_producto/<int:pk>', delete_producto, name="delete_producto"),
    
    # _________ API _________-
    
    path('api/productos', ApiPRoducts.as_view(), name="apiProducts"),
    path('api/productos/<int:pk>', ApiProduct.as_view(), name="apiProduct"),
    path('api/carrito', ApiCarritos.as_view(), name="apiCarrito"),
    path('api/carrito/<int:pk>', ApiCarrito.as_view(), name="apiCarrito"),
    path('api/donaciones', ApiDonaciones.as_view(), name="apiDonaciones"),
    path('api/donaciones/<int:pk>', ApiDonacion.as_view(), name="apiDonaciones"),
    path('api/pago', ApiPagos.as_view(), name="apiPago"),
    path('api/pago/<int:pk>', ApiPago.as_view(), name="apiPago"),
    path('api/cliente', ApiClientes.as_view(), name="apiPago"),
    path('api/cliente/<int:pk>', ApiCliente.as_view(), name="apiPago"),
]
