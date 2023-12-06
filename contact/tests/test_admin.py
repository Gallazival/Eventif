from django.test import TestCase
from contact.admin import ContatoModelAdmin, Contato, admin
from unittest.mock import Mock

class ContatoModelAdminTest(TestCase):
    def setUp(self):
        Contato.objects.create(
            nome="Enzo Hsu",
            email="enzo.hsu@aluno.riogrande.ifrs.edu.br",
            numero="53912345678",
            mensagem="Quero participar!"
        )
        self.model_admin = ContatoModelAdmin(Contato, admin.site)

    def test_foi_respondido(self):
        self.assertIn('respondido', self.model_admin.actions)

    def test_todos_respondidos(self):
        self.call_action()
        self.assertEqual(1, Contato.objects.filter(respondido=True).count())

    def test_message(self):
        self.call_action()
        self.mock.assert_called_once_with(
            None, '1 email foi respondido')

    def call_action(self):
        queryset = Contato.objects.all()
        self.mock = Mock()
        old_message_user = ContatoModelAdmin.message_user

        ContatoModelAdmin.message_user = self.mock

        self.model_admin.respondido(None, queryset)

        ContatoModelAdmin.message_user = old_message_user