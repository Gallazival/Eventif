from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contato

class contact_form(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'numero', 'mensagem']

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        partes = [w.capitalize() for w in nome.split()]
        return ' '.join(partes)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        numero = cleaned_data.get('numero')

        if not email and not numero:
            raise ValidationError('Informe seu email ou telefone')

        return cleaned_data
