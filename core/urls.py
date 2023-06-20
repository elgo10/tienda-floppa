from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('login/',  login, name="login"),
    path('registro/', registro),
    path('transferencia/', transferencia)
]