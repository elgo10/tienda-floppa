from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Choices

edChoices = (('Doctorado', 'Doctorado'),('Magister','Magister'),('Profesional','Profesional'))
regionChoices = (('Metropolitana', 'Metropolitana'),('Arica y parinacota', 'Arica y parinacota'),
                ('Tarapaca', 'Tarapaca'),('Atacama', 'Atacama'),('Coquimbo', 'Coquimbo'),
                ('Valparaiso', 'Valparaiso'),("Libertador Bernardo O'Higgins", "Libertador Bernardo O'Higgins"),
                ('Maule', 'Maule'),('BioBio', 'BioBio'),('Araucania', 'Araucania'),('Los rios', 'Los rios'),
                ('Los lagos', 'Los lagos'), ('Aysen', 'Aysen'),('Magallanes y de la Antártica Chilena', 'Magallanes y de la Antártica Chilena'))


class RegistroForm(UserCreationForm):
    
    region = forms.CharField(label='Region', max_length=200, widget=forms.Select(choices=regionChoices))
    nivelEducacional = forms.CharField(label='Nivel Educacional',max_length=200, widget=forms.Select(choices=edChoices))
    rut = forms.CharField(max_length=100, label='RUT')
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido = forms.CharField(max_length=100, label='Apellido')
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','rut', 'nombre', 'apellido','email', 'region', 'nivelEducacional']
        
        
        widgets = {
            'region': forms.Select(choices="regionChoices",attrs={'class': 'form-control'} ),
            'nivelEducacional': forms.Select(choices="edChoices",attrs={'class': 'form-control'} )
        }