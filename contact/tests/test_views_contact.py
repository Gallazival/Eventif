from django.core import mail
from django.test import TestCase
from contact.forms import contact_form

class teste_get(TestCase):
    def setUp(self):
        self.response = self.client.get('/contato/')

    def test_get(self):
        response = self.client.get('/contato/')
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_has_form(self):
        form = self.response.context["form"]
        self.assertIsInstance(form, contact_form)

class teste_post_e_valido(TestCase):
    def setUp(self):
        data = {'nome' : "Enzo Hsu",
                'email' : "enzo.hsu@aluno.riogrande.ifrs.edu.br",
                'numero' : "53-99973-1504",
                'mensagem' : "Funcionou!"}
        self.response = self.client.post('/contato/', data)

    def test_post(self):
        self.assertEqual(302, self.response.status_code)

    def test_enviou_email(self):
        self.assertTrue(mail.outbox)


class teste_post_e_invalido(TestCase):
    def setUp(self):
        self.response = self.client.post('/contato/', {})

    def test_post(self):
        self.assertEqual(200, self.response.status_code)

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, contact_form)

    def test_form_has_error(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)
