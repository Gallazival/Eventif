from django.db import models
from django.shortcuts import resolve_url as r 

class ContactSpeaker(models.Models):
    KINDS = (
        ('E', 'Email'),
        ('P', 'Telefone')
    )
    speaker = models.ForeignKey('Speaker', 'Speaker', on_delete=models.CASCADE )
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=225)

    class Meta:
        verbose_name = 'contato'
        varbose_name_plural = 'contatos'



class Speaker(models.Model):
    name = models.CharField('nome', max_length=225)

# Create your models here.
