from django import forms
from catalogo.models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'categoria', 'fecha_publicacion', 'isbn']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ingrese el título del libro'}),
            'autor': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del autor'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'placeholder': 'Ingrese el ISBN del libro'}),
        }

