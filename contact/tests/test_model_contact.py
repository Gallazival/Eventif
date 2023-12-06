from datetime import datetime
from django.test import TestCase
from contact.models import Contato


class ContatoModelTest(TestCase):
    def setUp(self):
        self.obj = Contato(
            nome="Enzo Hsu",
            email="enzo.hsu@aluno.riogrande.ifrs.edu.br",
            numero="53912345678",
            mensagem = "Quero participar!"
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Contato.objects.exists())

    def test_respondido(self):
        self.assertIsInstance(self.obj.hr_enviada, datetime)

    def test_str(self):
        self.assertEqual('Enzo Hsu', str(self.obj))
