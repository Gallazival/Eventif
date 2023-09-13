from django import forms 

class contact_form(forms.Form):
    nome = forms.CharField(label="Nome")
    email = forms.EmailField(label="Email")
    numero = forms.CharField(label="Número do telefone")
    mensagem = forms.CharField(label="Mensagem")