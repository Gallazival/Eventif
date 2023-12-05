<<<<<<< HEAD
from django import forms
=======
from django import forms 
>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f
from django.core.exceptions import ValidationError
from subscriptions.models import Subscription
from subscriptions.validators import validate_cpf

<<<<<<< HEAD

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        self.cleaned_data = super().clean()
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu email ou telefone')
=======
def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números', 'digits')
    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números', 'length')

class SubscriptionFormOld(forms.Form):
    name = forms.CharField(label="Nome")
    cpf = forms.CharField(label="CPF", validators=[validate_cpf])
    email = forms.EmailField(required=False)
    phone = forms.CharField(label="Telefone", required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.captalize() for w in name.split()]
        return ' '.join(words)
    
    def clean(self):
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone') :
            raise ValidationError('Informe seu email ou telefone')
        
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']
>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f
