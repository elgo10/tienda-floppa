from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistroForm(UserCreationForm):

    region = forms.CharField(max_length=200)
    nivelEducacional = forms.CharField(max_length=200)
    
    # edChoices = (('Doctorado', 'Doctorado'),('Magister','Magister'),('Profesional','Profesional'))
    # regionChoices = (('Metropolitana', 'Metropolitana'),('Arica y parinacota', 'Arica y parinacota'),
    #                 ('Tarapaca', 'Tarapaca'),('Atacama', 'Atacama'),('Coquimbo', 'Coquimbo'),
    #                 ('Valparaiso', 'Valparaiso'),("Libertador Bernardo O'Higgins", "Libertador Bernardo O'Higgins"),
    #                 ('Maule', 'Maule'),('BioBio', 'BioBio'),('Araucania', 'Araucania'),('Los rios', 'Los rios'),
    #                 ('Los lagos', 'Los lagos'), ('Aysen', 'Aysen'),('Magallanes y de la Antártica Chilena', 'Magallanes y de la Antártica Chilena'))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'region', 'nivelEducacional']
        
        widgets = {
            'region': forms.Select(attrs={'class': 'form-control'} ),
            'nivelEducacional': forms.Select(attrs={'class': 'form-control'} )
        }

class iniciarSesion(AuthenticationForm):
    class Meta:
        fields = '__all__'