from django.test import TestCase
from products.models import Product
from bag.context_processors import bag_contents, calculate_bag_total
from products.models import Category


class BagContextProcessorTestCase(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Some description",
            price=15.00,
            stock=5,
            color="Blue",
        )

        self.bag = {f"{self.product.id}_M": 3}

    def test_calculate_bag_total(self):
        total = calculate_bag_total(self.bag)
        self.assertEqual(total, 15.00 * 3)

    def test_bag_contents(self):
        class DummyRequest:
            session = {"bag": self.bag}

        context = bag_contents(DummyRequest())
        self.assertEqual(context["total"], 15.00 * 3)
        self.assertEqual(context["product_count"], 3)
        self.assertEqual(context["grand_total"], 15.00 * 3)
        self.assertEqual(len(context["bag_items"]), 1)
