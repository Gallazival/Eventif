from django.test import TestCase

from contact.forms import contact_form


class test_contact_form(TestCase):
    def setUp(self):
        self.form = contact_form()
        self.response = self.client.get('/contato/')

    def test_tem_campo(self):
        self.assertListEqual(list(self.form.fields), ['nome', 'email', 'numero', 'mensagem'])
   
    def test_tem_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')
