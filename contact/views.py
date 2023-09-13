from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from contact.forms import contact_form
from django.core import mail
from django.template.loader import render_to_string

def _enviar(assunto, de_, para, arquivo, conteudo):
    body = render_to_string(arquivo, conteudo)
    mail.enviar(assunto, body, de_, [de_, para])

def email(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            _enviar('Confirmação de novo contato',
                settings.DEFAULT_FROM_EMAIL, 
                form.cleaned_data['email'], 
                'contact/contact_email.txt', 
                form.cleaned_data)

            messages.success(request, 'Inscrição realizada com sucesso!')
            return HttpResponseRedirect("/contato/")
            
        else:
            return render(request, "contact/contact_form.html", {'form': form})
    
    else:
        return render(request, 'contact/contact_form.html', {'form': contact_form()})

