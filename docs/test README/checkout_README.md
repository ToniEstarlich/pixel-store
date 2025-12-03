## Comeback [README](../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
# checkout/test/
## test_views.py
**Test** 🟥
```python
def test_checkout_get_with_empty_bag_redirects(self):
    self.client.login(username='testuser', password='testpass')
    response = self.client.get(reverse('checkout'))
    self.assertRedirects(response, reverse('products_list'))
```

**Checks** 🟩

- Redirects when bag is empty

- Only accessible flow when cart has items

**Test** 🟥
```python
def test_checkout_success_view_ok(self):
    order = Order.objects.create(... )  # create order in DB
    self.client.login(username='testuser', password='testpass')
    session = self.client.session
    session['bag'] = {}
    session.save()

    url = reverse('checkout_success', args=[order.order_number])
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'checkout/checkout_success.html')
```

**Checks** 🟩

- Checkout success page loads for a valid order

- Uses correct template

- Session bag handling works
## test_models.py
**Test** 🟥
```python
def test_generate_order_number_on_save(self):
    order = Order.objects.create(... )
    self.assertTrue(order.order_number)
    self.assertEqual(len(order.order_number), 32)
```

**Checks** 🟩

- ``order_number`` auto-generated on save

- ``Format/length`` (32 chars) validated
## test_form.py
**Test** 🟥
```python
def test_order_form_valid_data(self):
    form = OrderForm(data={
        'full_name': 'Test User',
        'email': 'test@example.com',
        'phone_number': '123456789',
        'country': 'UK',
        'postcode': 'AB12CD',
        'town_or_city': 'London',
        'street_address1': '123 Street',
    })
    self.assertTrue(form.is_valid())
```

**Checks** 🟩

- Form validates correct data

- All required fields accepted
## Comeback [README](../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)