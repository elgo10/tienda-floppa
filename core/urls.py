from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('registro/', registrarse, name="registro"),
    path('transferencia/', transferencia),
    path('donaciones/', donaciones, name="donaciones")
]