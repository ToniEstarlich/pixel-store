from django.test import TestCase
from products.models import Category, Product


class ProductModelsTests(TestCase):

    def test_category_str(self):
        """El __str__ de Category devuelve su nombre"""
        category = Category.objects.create(name="My Category")
        self.assertEqual(str(category), "My Category")

    def test_product_str(self):
        # the product return name
        category = Category.objects.create(name="Another Category")
        product = Product.objects.create(
            name="My Product",
            description="A product",
            price=19.99,
            stock=5,
            size="L",
            color="Blue",
            category=category,
        )
        self.assertEqual(str(product), "My Product")
