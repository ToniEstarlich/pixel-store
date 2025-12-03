## Comeback [README](../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
# home/test/
## test_views.py
**Test** 🟥
```python
def test_index_view_status_code_and_template(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'home/index.html')
    self.assertIn('timestamp', response.context)
```

**Checks** 🟩

- Home page returns 200

- Correct template used

- Context includes timestamp

**Test** 🟥
```python
def test_faqs_view_status_code_and_template(self):
    response = self.client.get(reverse('faqs'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'home/faqs.html')
```

**Checks** 🟩

- FAQs page returns 200

- Correct template used
## test_context_processor.py
**Test** 🟥
```python
def test_timestamp_processor_returns_timestamp(self):
    request = RequestFactory().get('/')
    context = timestamp(request)
    self.assertIn('timestamp', context)
    self.assertIsInstance(context['timestamp'], int)
```

**Checks** 🟩

- **Context processor** injects timestamp key

- Value is an integer
## Comeback [README](../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)