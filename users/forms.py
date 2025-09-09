from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class CustomRegisterForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):
        user = super(CustomRegisterForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'default_phone_number',
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_postcode',
            'default_country',
            'default_county',
        ]

        labels = {
            'default_phone_number': 'Phone number',
            'default_street_address1': 'Street address 1',
            'default_street_address2': 'Street address 2',
            'default_town_or_city': 'Town / City',
            'default_postcode': 'Postcode',
            'default_country': 'Country',
            'default_county': 'County',
        }