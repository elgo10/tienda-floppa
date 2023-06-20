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