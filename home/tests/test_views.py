from django.test import TestCase
from django.urls import reverse

class HomeViewsTests(TestCase):

    def test_index_view_status_code_and_template(self):
        
        # the index return 200 and the template is correct
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertIn('timestamp', response.context)

    def test_faqs_view_status_code_and_template(self):
        
        # view FAQs return 200 and the template is correct
        response = self.client.get(reverse('faqs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/faqs.html')
