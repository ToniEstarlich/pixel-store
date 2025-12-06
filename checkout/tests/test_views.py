from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import UserProfile
from checkout.models import Order


class SimpleCheckoutViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.profile = UserProfile.objects.create(user=self.user)

    def test_checkout_get_with_empty_bag_redirects(self):

        # the bag is emply
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("checkout"))
        self.assertRedirects(response, reverse("products_list"))

    def test_checkout_success_view_ok(self):

        # checkout success
        order = Order.objects.create(
            user_profile=self.profile,
            full_name="Test User",
            email="test@example.com",
            phone_number="123456789",
            country="UK",
            town_or_city="London",
            street_address1="123 Street",
            original_cart="{}",
            stripe_pid="testpid",
        )

        self.client.login(username="testuser", password="testpass")
        session = self.client.session
        session["bag"] = {}
        session.save()

        url = reverse("checkout_success", args=[order.order_number])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout_success.html")
