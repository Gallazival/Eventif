from django.test import TestCase
from subscriptions.admin import SubscriptionModelAdmin, Subscription, admin

class SubscriptionModelAdminTest(TestCase):
    def test_has_action(self):
        model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        self.assertIn('mark_as_paid', model_admin.actions)

    def test_mark_all(self):
        Subscription.objects.create(
            name ="Enzo Hsu",
            cpf="12345678901",
            email="enzoyhsu@gmail.com",
            phone="53999731504"
        )
        queryset = Subscription.objects.all()

        model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        model_admin = mark_as_paid()