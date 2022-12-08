from django import forms

# Mi formulario
class InputForm(forms.Form):

    Foto = forms.CharField(max_length = 100)

    Titulo = forms.CharField(max_length = 4)

    Descripción = forms.CharField(max_length = 80)

    Tags = forms.CharField(max_length = 50)

    URL_GIT = forms.CharField(max_length = 150)