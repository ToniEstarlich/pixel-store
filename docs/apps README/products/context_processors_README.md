## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
# pixel-store/clothing_store/
**setting**🟦
```python
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                ...
                'products.context_processors.get_categories',
            ],
        },
    },
]
```
# pixel-store/products/models.py
- The ``Category`` model defines product categories with unique names, used to organize items in the store.

**models** 🟦
```python
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories" # <-- this change the plural correct 

    def __str__(self):
        return self.name
```
# pixel-store/products/context_processors.py
## get_categories
**function** 🟩
```python
def get_categories(request):
    from .models import Category
    categories = Category.objects.all()
    return {
        'categories': categories
        }
```
**html** 🟧 **Jinja** ⬜
``pixel-store/templates/includes/mobile-top-header.html``
```html
{% for category in categories %}
    <a class="nav-link" href="{% url 'products_list' %}?category={{ category.name }}">{{ category.name }}</a>
{% endfor %}
```
- ``get_categories(request):`` Fetches all ``Category`` objects from the database and makes them available in templates as ``categories``.
## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)