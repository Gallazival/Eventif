from django.db import models


class Contato(models.Model):
    nome = models.CharField('nome', max_length=200)
    email = models.EmailField('e-mail', blank=True)
    numero = models.CharField('numero', max_length=20, blank=True)
    mensagem = models.TextField('mensagem')
    hr_enviada = models.DateTimeField('enviado em', auto_now_add=True)
    respondido = models.BooleanField('respondido', default=False)

    class Meta:
        verbose_name_plural = "contatos"
        verbose_name = "contato"
        ordering = ['-hr_enviada',]

    def __str__(self):
        return self.nome