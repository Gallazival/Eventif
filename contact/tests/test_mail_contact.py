from django.core import mail
from django.test import TestCase


class teste_email(TestCase):
    def setUp(self):
        data = {'nome' : "Enzo Hsu",
                'email' : "enzo.hsu@aluno.riogrande.ifrs.edu.br",
                'numero' : "53-99973-1504", 
                'mensagem' : "Funcionou!"}
        self.response = self.client.post('/contato/', data)
        self.email = mail.outbox[0]

    def test_assunto_email(self):
        expect = "Confirmação de novo contato"
        self.assertEqual(expect, self.email.subject)

    def test_email_destinatario(self):
        expect = "contato@eventif.com.br"
        self.assertEqual(expect, self.email.from_email)

    def test_email_participantes(self):
        expect = ['contato@eventif.com.br', 'enzo.hsu@aluno.riogrande.ifrs.edu.br']
        self.assertEqual(expect, self.email.to)

    def test_email_conteudo(self):
        contents = ['Enzo Hsu',
                    'enzo.hsu@aluno.riogrande.ifrs.edu.br',
                    '53-99973-1504',
                    'Funcionou!']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
   
 