from django.test import TestCase
<<<<<<< HEAD
from django.core import mail
from django.shortcuts import resolve_url as r


class MailTest(TestCase):
    def setUp(self):
        data = dict(name="Cleber Fonseca",
                    cpf="12345678901",
                    email="profcleberfonseca@gmail.com",
                    phone="53-91234-5678")

=======
from django.shortcuts import resolve_url as r

class MailTest(TestCase):
    def setUp(self):
        data = dict(name="Diego",
                    cpf="12345678901",
                    email="diego.avila@aluno.riogrande.ifrs.edu.br",
                    phone="53-99101-1002")
>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f
        self.response = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = "Confirmação de inscrição"
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_sender(self):
        expect = "contato@eventif.com.br"
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
<<<<<<< HEAD
        expect = ['contato@eventif.com.br', 'profcleberfonseca@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Cleber Fonseca',
                    '12345678901',
                    'profcleberfonseca@gmail.com',
                    '53-91234-5678']
=======
        expect = ['contato@eventif.com.br',
                  'diego.avila@aluno.riogrande.ifrs.edu.br']
        self.assertEqual(expect, self.email.to)

    def test_subscription_body(self):
        contents = ['Diego',
                    '12345678901',
                    'diego.avila@aluno.riogrande.ifrs.edu.br',
                    '53-99101-1002']
>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
