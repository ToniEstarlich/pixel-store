## Comeback [README](../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
# bag/test/
## test_views.py
Test 🟥
```python
def test_view_bag_page_status_code(self):
    response = self.client.get(reverse('view_bag'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'bag/bag.html')
```

Checks 🟩

1- Bag page returns 200

2- Correct template used

Test 🟥
```python
def test_add_to_bag(self):
    response = self.client.post(
        reverse('add_to_bag', args=[self.product.id]),
        {'quantity': 2, 'size': 'M'},
        HTTP_X_REQUESTED_WITH='XMLHttpRequest'
    )
    self.assertEqual(response.status_code, 200)
    self.assertIn('grand_total', response.json())
```

Checks 🟩

1- AJAX add-to-bag returns 200

2- Response includes ``grand_total`` in JSON

Test 🟥
```python
def test_remove_from_bag(self):
    session = self.client.session
    session['bag'] = {f'{self.product.id}_M': 2}
    session.save()

    response = self.client.post(reverse('remove_from_bag', args=[self.product.id]), {'size': 'M'})
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('view_bag'))
```

Checks 🟩

1- Remove action redirects to bag view

2- Item removed from session

Test 🟥
```python
def test_clear_bag(self):
    session = self.client.session
    session['bag'] = {f'{self.product.id}_M': 2}
    session.save()

    response = self.client.get(reverse('clear_bag'))
    self.assertEqual(response.status_code, 302)
    session = self.client.session
    self.assertEqual(session['bag'], {})
```

Checks 🟩
1- Clear bag redirects
2- Session bag is empty after clear
## test_url.py
Test 🟥
```python
def test_view_bag_url_resolves(self):
    url = reverse('view_bag')
    self.assertEqual(resolve(url).func, views.view_bag)
```

Checks 🟩

- view_bag URL resolves to correct view function

Test 🟥
```python
def test_add_to_bag_url_resolves(self):
    url = reverse('add_to_bag', args=[1])
    self.assertEqual(resolve(url).func, views.add_to_bag)
```

Checks 🟩

- add_to_bag URL resolves correctly
 
 (And same for ``remove_from_bag`` and ``clear_bag``)
## test_context_processor.py
Test 🟥
```python
def test_calculate_bag_total(self):
    total = calculate_bag_total(self.bag)
    self.assertEqual(total, 15.00 * 3)
```

Checks 🟩

- ``calculate_bag_total`` returns correct total for quantities

Test 🟥
```python
def test_bag_contents(self):
    class DummyRequest:
        session = {'bag': self.bag}

    context = bag_contents(DummyRequest())
    self.assertEqual(context['total'], 15.00 * 3)
    self.assertEqual(context['product_count'], 3)
    self.assertEqual(context['grand_total'], 15.00 * 3)
    self.assertEqual(len(context['bag_items']), 1)
```

Checks 🟩

1- ``bag_contents`` returns total,``product_count``, ``grand_total`` correctly

2- ``bag_items`` contains expected entries
## Comeback [README](../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)