from django.test import TestCase

from subscriptions.forms import SubscriptionForm


<<<<<<< HEAD
class subscriptionFormTest(TestCase):
=======
class SubscriptionFormTest(TestCase):        

>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f
    def test_form_has_fields(self):
        self.form = SubscriptionForm()
        self.assertSequenceEqual(
            ['name', 'cpf', 'email', 'phone'], list(self.form.fields))
<<<<<<< HEAD

    def test_cpf_has_digit(self):
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        form = self.make_validated_form(cpf='123456')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_capitalized(self):
        form = self.make_validated_form(name='CLEBER fonseca')
        self.assertEqual('Cleber Fonseca', form.cleaned_data['name'])
=======
        
    def test_cpf_has_digit(self):
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_cpf_has_11_digits(self):
        form = self.make_validated_form(cpf ='123456')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_mest_be_captalized(self):
        form = self.make_validated_form(name='ENZO hsu')
        self.assertEqual('Enzo Hsu', form.cleaned_data['name'])
>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f

    def test_email_is_optional(self):
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
<<<<<<< HEAD
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))
=======
        form= self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors)) 
>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        error_list = errors[field]
        exception = error_list[0]
<<<<<<< HEAD
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        error_list = errors[field]
        self.assertListEqual([msg], error_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Cleber Fonseca', cpf='12345678901',
                     email='profcleberfonseca@gmail.com', phone='53-912345678')
=======
        self.assertListEqual(code, exception.code)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Enzo Hsu', cpf='ABCD5678901',
                    email='enzoyhsu@gmail.com', phone='53999731504')
>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
<<<<<<< HEAD
=======

class TemplateRegrassionTest(TestCase):
    def test_template_has_nonfield_errors(self):
        invalid_data = dict(name='Enzo Hsu', cpf='12345678901')
        response = self.client.post(r('subscriptions:new'), invalid_data)
        self.assertContains(response, '<ul class="errorlist nonfield">')
>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f
