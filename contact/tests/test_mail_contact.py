from django.core import mail
from django.test import TestCase


class MailTest(TestCase):
    def setUp(self):
        data = dict(name="Enzo Hsu",
                    cpf="12345678901",
                    email="enzo.hsu@aluno.riogrande.ifrs.edu.br",
                    phone="53-99973-1504")
        self.response = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = "Confirmação de inscrição"
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_sender(self):
        expect = "contato@eventif.com.br"
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventif.com.br',
                  'enzo.hsu@aluno.riogrande.ifrs.edu.br']
        self.assertEqual(expect, self.email.to)

    def test_subscription_body(self):
        contents = ['Enzo Hsu',
                    '12345678901',
                    'enzo.hsu@aluno.riogrande.ifrs.edu.br',
                    '53-99973-1504']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)