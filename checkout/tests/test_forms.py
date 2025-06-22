from django.test import TestCase
from checkout.forms import OrderForm

class OrderFormTest(TestCase):

    def test_order_form_valid_data(self):
       
        # data and formulary is correct
        form = OrderForm(data={
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '123456789',
            'country': 'UK',
            'postcode': 'AB12CD',
            'town_or_city': 'London',
            'street_address1': '123 Street',
            'street_address2': '',
            'county': 'CountyName',
        })
        self.assertTrue(form.is_valid())
