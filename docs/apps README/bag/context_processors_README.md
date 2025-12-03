## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
# pixel-store/clothing_store/
**setting**🟦
```python
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                ...
               'bag.context_processors.bag_contents', 
            ],
        },
    },
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
# pixel-store/bag/context_processors.py

## bag_contents
**function** 🟩
```python
def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    ...
    return {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }
```
**html** 🟧 **Jinja** ⬜
``pixel-store/templates/includes/main-nav.html``
```html
<a class="nav-link text-white" href="{% url 'view_bag' %}">
    <i class="fas fa-shopping-bag"></i>
    <span id="bag-total">
      £{% if grand_total %}{{ grand_total|floatformat:2 }}{% else %}0.00{% endif %}
    </span>
</a>
```
``bag_contents(request)``

- Reads the bag from the session.

- Loops through each item key (productID_size).

- Fetches the product, calculates subtotal, total price, and product count.

Returns a dictionary with bag items, total price, product count, and grand total.
## calculate_bag_total(bag)
**function** 🟩
```python
def calculate_bag_total(bag):
    total = 0
    for item_key, quantity in bag.items():
        try:
            product = Product.objects.get(pk=int(item_id))
            ...
        total += product.price * quantity
    return total
```
**html** 🟧 **Jinja** ⬜
```html
<p><strong>Total:</strong> £{{ grand_total|floatformat:2 }}</p>
```

``calculate_bag_total(bag)``

- Loops through the bag items.

- Retrieves each product and sums their prices × quantity.

- Returns the total bag cost.
## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)