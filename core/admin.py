from django.contrib import admin
from .models import  *
# Register your models here.


admin.site.register(Cliente)
admin.site.register(Carrito)
admin.site.register(Producto)
admin.site.register(Pagar)
admin.site.register(Donaciones)

