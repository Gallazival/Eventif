from django.test import TestCase
<<<<<<< HEAD
from core.models import Speaker, ContactSpeaker
from django.core.exceptions import ValidationError


=======
from core.models import Speaker, ContactSpeaker 
from django.core.exceptions import ValidationError

>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f
class ContactSpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name="Cleber Fonseca",
            slug="cleber-fonseca",
            photo="https://cleberfonseca.com.br/img/perfil.png"
        )
<<<<<<< HEAD

    def test_email(self):
        contact = ContactSpeaker.objects.create(
            speaker=self.speaker,
            kind=ContactSpeaker.EMAIL,
            value='profcleberfonseca@gmail.com'
=======
    def test_email(self):
        contact = ContactSpeaker.objects.create(
            speaker=self.speaker,
            kind='E',
            value='profclaberfonseca@gmail.com',
>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f
        )
        self.assertTrue(ContactSpeaker.objects.exists())

    def test_phone(self):
        contact = ContactSpeaker.objects.create(
            speaker=self.speaker,
<<<<<<< HEAD
            kind=ContactSpeaker.PHONE,
            value='53-912345678'
=======
            kind='P',
            value='53-912345678',
>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f
        )
        self.assertTrue(ContactSpeaker.objects.exists())

    def test_choices(self):
        contact = ContactSpeaker.objects.create(
            speaker=self.speaker,
            kind='A',
<<<<<<< HEAD
            value='B'
=======
            kind='B'
>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f
        )
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = ContactSpeaker(
<<<<<<< HEAD
            speaker=self.speaker,
            kind=ContactSpeaker.EMAIL,
            value='profcleberfonseca@gmail.com'
        )
        self.assertEqual('profcleberfonseca@gmail.com', str(contact))
=======
            speaker
        )
>>>>>>> aabad51da67e85a9357f4b8a22d660461fddae1f
