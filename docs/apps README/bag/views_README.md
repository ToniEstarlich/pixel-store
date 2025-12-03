## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
# pixel-store/clothing_store/
**setting**🟦
```python
INSTALLED_APPS = [
    # my apps
    'bag',
]
```
**urls**🟩
```python
urlpatterns = [
    path('bag/', include('bag.urls')),
]
```
# pixel-store/bag/models.py
**models** 🟦
- represents an item in a user's shopping bag, linking a user to a specific product (with optional size), enforcing uniqueness per ``user/product/size``, and providing quantity and subtotal calculation.

```python
class BagItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bag_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, null=True, blank=True) 
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product', 'size')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} ({self.size}) for {self.user.username}"

    def subtotal(self):
        return self.product.price * self.quantity
```

# pixel-store/bag/views.py
## view_bag
**function** 🟩
```python
def view_bag(request):
    if request.user.is_authenticated:
    ...
    return render(request, 'bag/bag.html', context)
```
**urls** 🟩
```python
urlpatterns = [
    path('', views.view_bag, name='view_bag'),
]
```
**html** 🟧 **Jinja** ⬜
```html
{% for item in bag_items %}
  <li class="list-group-item d-flex align-items-center">

    {% if item.product.image %}
    <img src="{{ item.product.image.url }}" alt="{{ item.product.name }}" width="60" height="60" class="mr-3">
    {% else %}
    <img src="{% static 'images/no-image.png' %}" alt="No image" width="60" height="60" class="mr-3">
    {% endif %}

    <div class="flex-grow-1">
      <strong>{{ item.product.name }}</strong> ({{ item.size }}) x{{ item.quantity }}
    </div>
    ...
```
``view_bag(request):``

- Loads the bag from session (or from the database if the user is logged in).

- Builds a list of items with product, size, quantity, and subtotal.

- Calculates total, delivery cost, and grand total.

- Renders the bag page.

## add_to_bag
**function** 🟩
```python
def add_to_bag(request, item_id):
    size = request.POST.get('size')
    ...
    return JsonResponse({
        'message': 'Product added to bag',
        'product_name': product.name,
        'image_url': product.image.url if product.image else '/static/images/no-image.png',
        'grand_total': f'{grand_total:.2f}'
    })
```
**urls** 🟩
```python
urlpatterns = [
    path('add/<int:item_id>/', views.add_to_bag, name='add_to_bag'),
]
```
**JS** 🟨
"This script ``pixel-store/static/js/add_to_bag.js`` sends the Add to Bag form via AJAX and updates the cart total without reloading the page."
```Javascript
document.addEventListener('DOMContentLoaded', () => {
  const forms = document.querySelectorAll('.add-to-bag-form');
  ...
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
```
**html** 🟧 **Jinja** ⬜
```html
<form method="post" action="{% url 'add_to_bag' product.id %}" class="add-to-bag-form">
      {% csrf_token %}
      ...
     <!-- SUBMIT BUTTON -->
    <div class="form-group mt-3">
      <button type="submit" class="btn btn-primary btn-block">Add to bag</button>
    </div>
</form>                        
```
``add_to_bag(request, item_id):``

- Gets size and quantity from the POST request.

- Adds or updates the item in the session bag (and in the database if the user is logged in).

- Returns a JSON response with product info and new total.
## remove_from_bag
**function** 🟩
```python
@require_POST
def remove_from_bag(request, item_id):
    size = request.POST.get('size')
    ...
    return redirect('view_bag')
```
**urls** 🟩
```python
urlpatterns = [
    path('bag/remove/<item_id>', views.remove_from_bag, name='remove_from_bag'),
]
```
**html** 🟧 **Jinja** ⬜
```html
<form action="{% url 'remove_from_bag' item.item_id %}" method="POST">
      {% csrf_token %}
      <input type="hidden" name="size" value="{{ item.size }}">
      <button type="submit">Remove</button>
</form>
```
``remove_from_bag(request, item_id):``

- Gets the size from POST and removes the item from session (and DB for logged-in users).

- Redirects to the bag page.
## clear_bag
The ``clear_bag`` view is implemented to empty the shopping bag from session and database, but it is currently not linked to any button in the UI.

**function** 🟩
```python
def clear_bag(request):
    request.session['bag'] = {}
    ...
    return redirect('view_bag')
```
**urls** 🟩
```python
urlpatterns = [
    path('clear/', views.clear_bag, name='clear_bag'),
]
```
**html** 🟧 **Jinja** ⬜
```html
<form action="{% url 'clear_bag' %}" method="post">
    {% csrf_token %}
    <button type="submit">Clear Bag</button>
</form>
```
``clear_bag(request):``

-  Empties the entire bag from session and DB (if logged in).

- Redirects to the bag page.

- "Implemented but not linked in the UI yet, kept for future use."
## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)