from django.db import models
from django.contrib.auth.models import User

# Create your models here.

edChoices = (('Doctorado', 'Doctorado'),('Magister','Magister'),('Profesional','Profesional'))
regionChoices = (('Metropolitana', 'Metropolitana'),('Arica y parinacota', 'Arica y parinacota'),
                    ('Tarapaca', 'Tarapaca'),('Atacama', 'Atacama'),('Coquimbo', 'Coquimbo'),
                    ('Valparaiso', 'Valparaiso'),("Libertador Bernardo O'Higgins", "Libertador Bernardo O'Higgins"),
                    ('Maule', 'Maule'),('BioBio', 'BioBio'),('Araucania', 'Araucania'),('Los rios', 'Los rios'),
                    ('Los lagos', 'Los lagos'), ('Aysen', 'Aysen'),('Magallanes y de la Antártica Chilena', 'Magallanes y de la Antártica Chilena'))

class Cliente(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=200, choices=regionChoices)
    nivelEducacional = models.CharField(max_length=200, choices=edChoices)
    rut = models.CharField(max_length=100, null=True)
    nombre = models.CharField(max_length=100, null=True)
    apellido = models.CharField(max_length=100, null=True)
    
    def __str__(self):    
        return self.nombre
    
class Producto(models.Model):
    
    nombre = models.CharField(max_length=100, null=True)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=200, null=True)
    marca = models.CharField(max_length=100, null=True)
    cantidad = models.IntegerField()
    img = models.ImageField()
    
    def __str__(self):
        return self.nombre
    
class Carrito(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField(blank=True, default=0)
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    def __str__(self):    
        return f'{self.user.id} | {self.productos.nombre}'


class Donaciones(models.Model):
    
    nombre = models.CharField(max_length=200)
    nro_tarjeta = models.IntegerField()
    fecha = models.DateField()
    ccv = models.IntegerField()
    cant = models.IntegerField()
    
    def __str__(self):
        
        return f'{self.id} | {self.nombre} | {self.fecha}'
    

class Pagar(models.Model):
    
    nombre = models.CharField(max_length=100)
    direccion =  models.CharField(max_length=100)
    nro_depto  = models.IntegerField(null=True, blank=True)
    region = models.CharField(max_length=200)
    comuna = models.CharField(max_length=100)
    cod_postal = models.IntegerField()
    # ____________ Tarjeta
    tarjeta_nom = models.CharField(max_length=100)
    nro_tarjeta = models.IntegerField()
    ccv = models.IntegerField()
    fecha = models.DateField()
    
    def __str__(self):
        
        return f'{self.id} | {self.nombre} | {self.fecha}'