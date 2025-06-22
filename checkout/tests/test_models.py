from django.test import TestCase
from checkout.models import Order

class OrderModelTest(TestCase):

    def test_generate_order_number_on_save(self):
        
        # the number what is generate is save
        order = Order.objects.create(
            full_name='Test User',
            email='test@example.com',
            phone_number='123456789',
            country='UK',
            town_or_city='London',
            street_address1='123 Street',
            original_cart='{}',
            stripe_pid='testpid',
        )
        self.assertTrue(order.order_number)
        self.assertEqual(len(order.order_number), 32)  
