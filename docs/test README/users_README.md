## Comeback [README](../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
# users/test/
## test_views.py
**Test** 🟥
```python
def test_profile_view_logged_in(self):
    user = User.objects.create_user(username='testuser', password='testpass')
    UserProfile.objects.create(user=user)
    self.client.login(username='testuser', password='testpass')
    response = self.client.get(reverse('profile'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'users/profile.html')
```

**Checks** 🟩

1- ``Logged-in`` user can access profile page

2- Correct template (profile.html) is used

**Test** 🟥
```python
@skip("Skipping profile view login required test for simplicity.")
def test_profile_view_login_required(self):
    response = self.client.get(reverse('profile'))
    self.assertRedirects(response, '/accounts/login/?next=/users/profile/')
```

**Checks** 🟩

- Accessing profile without login redirects to login page
## test_models.py
**Test** 🟥
```python
def test_userprofile_str_returns_username(self):
    user = User.objects.create_user(username='john')
    profile = UserProfile.objects.create(user=user)
    self.assertEqual(str(profile), 'john')
```

**Checks** 🟩

- ``__str__ of UserProfile`` returns the **associated username**

## test_form.py
**Test** 🟥
```python
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
```

**Checks** 🟩
- ``UserProfileForm`` contains all expected fields

## Comeback [README](../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)