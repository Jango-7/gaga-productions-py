from django import forms

class Formulario(forms.Form):
    artista = forms.CharField(max_length=100)
    cancion = forms.CharField(max_length=100)
    tonalidad = forms.CharField(max_length=20)


class SearchForm(forms.Form):
    query = forms.CharField(label='Podes buscar artistas')
