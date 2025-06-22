from django.test import TestCase, RequestFactory
from products.context_processors import get_categories
from products.models import Category

class ContextProcessorTests(TestCase):

    def setUp(self):
        # we create a example category
        self.category = Category.objects.create(name='Example Category')

    def test_get_categories_returns_categories(self):
        
        factory = RequestFactory()
        request = factory.get('/')
        context = get_categories(request)
        self.assertIn('categories', context)
        categories = context['categories']
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0].name, 'Example Category')

