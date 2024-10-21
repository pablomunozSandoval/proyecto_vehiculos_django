from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']

    # Campos de texto personalizados
    modelo = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 1, 'style': 'resize: horizontal;' 
        })
    )
    serial_carroceria = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 1, 'style': 'resize: horizontal;'
        })
    )
    serial_motor = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 1, 'style': 'resize: horizontal;'
        })
    )
    