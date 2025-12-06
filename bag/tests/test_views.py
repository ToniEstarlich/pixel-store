from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product


class BagViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(name="Test Product", price=10.00)

    def test_view_bag_page_status_code(self):
        response = self.client.get(reverse("view_bag"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bag/bag.html")

    def test_add_to_bag(self):
        response = self.client.post(
            reverse("add_to_bag", args=[self.product.id]),
            {"quantity": 2, "size": "M"},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("grand_total", response.json())

    def test_remove_from_bag(self):
        session = self.client.session
        session["bag"] = {f"{self.product.id}_M": 2}
        session.save()

        response = self.client.post(
            reverse("remove_from_bag", args=[self.product.id]), {"size": "M"}
        )
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertRedirects(response, reverse("view_bag"))
        session = self.client.session
        self.assertNotIn(f"{self.product.id}_M", session["bag"])

    def test_clear_bag(self):
        session = self.client.session
        session["bag"] = {f"{self.product.id}_M": 2}
        session.save()

        response = self.client.get(reverse("clear_bag"))
        self.assertEqual(response.status_code, 302)
        session = self.client.session
        self.assertEqual(session["bag"], {})
