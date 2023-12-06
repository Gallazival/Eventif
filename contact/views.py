from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string

from contact.forms import contact_form


def new(request):
    if request.method == 'POST':
        return email(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'contact/contact_form.html', {"form": contact_form()})


def email(request):
    form = contact_form(request.POST)

    if not form.is_valid():
        return render(request, 'contact/contact_form.html', {'form': form})

    envio = form.save()

    _enviar('Confirmação de inscrição',
               settings.DEFAULT_FROM_EMAIL,
               envio.email,
               'contact/subscription_email.txt',
               {'subscription': envio})

    return HttpResponseRedirect(r('contact'))


def _enviar(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])