from django import forms
from .models import conciertos

class cargaConciertos(forms.ModelForm):
    class Meta:
        model = conciertos
        fields = ["ARTISTAS", "LUGAR", "FECHA"]
        widgets ={
            'FECHA': forms.DateInput(attrs={'type': 'date'}),
        }
