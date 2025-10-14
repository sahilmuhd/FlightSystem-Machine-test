from django import forms
from .models import AirportRoute

class AirportRouteForm(forms.ModelForm):
    class Meta:
        model = AirportRoute
        fields = ['airport_code', 'position', 'duration']
        widgets = {
            'airport_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Airport Code'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration in minutes'}),
        }

from django import forms

class SearchForm(forms.Form):
    direction = forms.ChoiceField(
        choices=[('Left', 'Left'), ('Right', 'Right')],
        label="Direction"
    )
    n = forms.IntegerField(label="Nth Node", min_value=1)


class ShortestRouteForm(forms.Form):
    source = forms.CharField(label="Source Airport Code")
    destination = forms.CharField(label="Destination Airport Code")

