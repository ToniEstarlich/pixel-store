## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
# pixel-store/clothing_store/
**setting**🟦
```python
INSTALLED_APPS = [
    # my apps
    'products',
]
```
**urls**🟩
```python
urlpatterns = [
    path('products/', include('products.urls')),
]
```
# pixel-store/products/models.py
- The ``Categor``y model defines product categories with unique names, used to organize items in the store.

**models** 🟦
```python
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories" # <-- this change the plural correct 

    def __str__(self):
        return self.name
```
- The ``Product`` model represents each store item with details like name, description, price, stock, size, color, category, and optional image.

**models** 🟦
```python
class Product(models.Model):

    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, unique=True, null=True, blank=True)
    description = models.TextField()
    ...
    def __str__(self):
        return self.name
```
# pixel-store/products/views.py

## product_list
**function** 🟩
```python
@login_required
def product_list(request):
    category_name = request.GET.get('category')
    ...
     return render(request, 'products/products_list.html', {
        'products': products,
        'categories': categories,
        'timestamp': now().timestamp(),
        'selected_category': category_name,
    })
```
**urls** 🟩
```python
urlpatterns = [
    path('', views.product_list, name='products_list'),
]
```
**html** 🟧 **Jinja** ⬜ ``pixel-store/products/templates/products/products_list.html``
```html
{% for product in products %}
        <div class="col-md-4 mb-4">
            <div class="card h-100 glass-card">
                {% if product.image %}
                <img src="{{ product.image.url }}" class="card-img-top" alt="{{ product.name }}">
                ...
                {% endif %}
                <div class="card-body">
                    <h5 class="card-title">{{ product.name }}</h5>
                    <p class="card-text">{{ product.description|truncatewords:20 }}</p>
                    <p class="card-text font-weight-bold">€{{ product.price }}</p>
                ...
{% endfor %}
```
``product_list(request):``

- Requires login.

- Gets optional ``category`` filter from the URL.

- Retrieves products (filtered or all) and all categories.

Renders the product list with a timestamp and the selected category.
## search
**function** 🟩
```python
def search(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'products/search_results.html', {
    'results': results, 
    'query': query,
    })
```
**urls** 🟩
```python
urlpatterns = [
    path('search/', views.search, name='search'),
]
```
**html** 🟧 **Jinja** ⬜

Search form (navbar):  
`pixel-store/templates/includes/mobile-top-header.html`
```html
<form method="GET" action="/products/search/" class="form-inline my-2">
      <input class="form-control mr-2 w-75" type="search" placeholder="Search" name="q">
      <button class="btn_search" type="submit"><i class="fas fa-search" aria-hidden="true"></i></button>
</form>
```
Search results template:  
`pixel-store/products/templates/products/search_results.html`
```html
<h2>Search results for "{{ query }}"</h2>

{% if results %}
  <ul>
    {% for product in results %}
      <li>{{ product.name }}</li>
    {% endfor %}
  </ul>
{% else %}
  <p>No products found.</p>
{% endif %}

```

``search(request):``

- Gets the ``q`` query string.

- Searches products whose name contains the query.

- Renders the search results page.
## product_detail
**function** 🟩
```python
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)
```
**urls** 🟩
```python
urlpatterns = [
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]
```
**html** 🟧 **Jinja** ⬜ ``pixel-store/products/templates/products/product_detail.html``
```html
<!-- Example product detail template -->
<h1>{{ product.name }}</h1>
<p>{{ product.description }}</p>
<p>Price: £{{ product.price|floatformat:2 }}</p>

{% if product.image %}
  <img src="{{ product.image.url }}" alt="{{ product.name }}">
{% else %}
  <p>No image available</p>
{% endif %}
```
``product_detail(request, product_id):``

- Gets a product by ID (404 if not found).

- Renders the product detail page.
## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)