from django.test import TestCase
from users.forms import UserProfileForm

class UserFormsTests(TestCase):

    def test_userprofile_form_fields(self):
        
        form = UserProfileForm()
        expected_fields = [
            'default_phone_number',
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_postcode',
            'default_country',
            'default_county',
        ]
        self.assertEqual(list(form.fields.keys()), expected_fields)
