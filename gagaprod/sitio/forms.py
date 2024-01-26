from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Búsqueda de artistas')


class Formulario(forms.Form):
    email = forms.EmailField()



