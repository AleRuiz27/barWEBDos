from django import forms
from .models import bandas_conciertos

class cargaConciertos(forms.ModelForm):
    class Meta:
        model = bandas_conciertos
        fields = ["ARTISTAS", "LUGAR", "FECHA"]
        widgets ={
            'FECHA': forms.DateInput(attrs={'type': 'date'}),
        }
