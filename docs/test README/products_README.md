## Comeback [README](../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
# products/test/
## test_views.py
**Test** 🟥
```python
def test_get_categories_returns_categories(self):
    factory = RequestFactory()
    request = factory.get('/')
    context = get_categories(request)
    self.assertIn('categories', context)
    categories = context['categories']
    self.assertEqual(len(categories), 1)
    self.assertEqual(categories[0].name, 'Example Category')
```

**Checks** 🟩

- **Context processor** returns categories key

- Categories list contains created categories
## test_models.py
**Test** 🟥
```python
def test_category_str(self):
    category = Category.objects.create(name='My Category')
    self.assertEqual(str(category), 'My Category')
```

**Checks** 🟩

- ``Category.__str__()`` returns the category name
## test_context_processor.py
**Test** 🟥
```python
def test_get_categories_returns_categories(self):
    factory = RequestFactory()
    request = factory.get('/')
    context = get_categories(request)
    self.assertIn('categories', context)
    categories = context['categories']
    self.assertEqual(len(categories), 1)
    self.assertEqual(categories[0].name, 'Example Category')
```

**Checks** 🟩

- **Context processor** returns categories key

- Categories list contains created categories
## Comeback [README](../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)