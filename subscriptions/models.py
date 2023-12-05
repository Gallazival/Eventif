from django.db import models
from subscriptions.validators import validate_cpf


class Subscription(models.Model):
    name = models.CharField('nome', max_length=200)
<<<<<<< HEAD
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    email = models.EmailField('e-mail', blank=True)
    phone = models.CharField('telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    paid = models.BooleanField('pago', default=False)
=======
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    paid = models.BooleanField(default=False)
>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f

    class Meta:
        verbose_name_plural = "inscrições"
        verbose_name = "inscrição"
        ordering = ['-created_at',]

    def __str__(self):
        return self.name
