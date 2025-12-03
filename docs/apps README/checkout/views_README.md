## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
# pixel-store/clothing_store/
**setting**🟦
```python
INSTALLED_APPS = [
    # my apps
    'checkout',
]
```
**urls**🟩
```python
urlpatterns = [
    path('checkout/', include('checkout.urls')),
]
```
# pixel-store/checkout/models.py
**models** 🟦
- The ``Order`` model stores all customer and payment details for a purchase, automatically generates an order number, and calculates order totals including delivery costs.

```python
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    ...
    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
    
    def update_total(self):
       ...
        self.save()
```
- The ``OrderLineItem`` model represents each product in the order, storing its quantity and computing its line total.

**models** 🟦
```python
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    ...
    def save(self, *args, **kwargs):
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
```
# pixel-store/checkout/forms.py
**form**🟦
```python
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'phone_number',
            'country', 'postcode', 'town_or_city',
            'street_address1', 'street_address2', 'county',
        )
```
# pixel-store/checkout/views.py
## CheckoutView
**function** 🟩
```python
class CheckoutView(View):
    def get(self, request):
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "Your bag is empty.")
            return redirect('products_list')
            ...
            request.session['bag'] = {} #this leave empty the bag
            return redirect(session.url, code=303)
        
        return render(request, 'checkout/checkout.html', {'form' : form})
```
**urls** 🟩
```python
urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
]
```
**html** 🟧 **Jinja** ⬜
``pixel-store/checkout/templates/checkout/checkout.html``
```html
<form method="post" class="checkout-form">
      {% csrf_token %}
      {{ form|crispy }}
      <button type="submit" class="checkout-button">Place Order</button>
</form>
```
``class CheckoutView.get():``

- Checks if the bag is empty; if it is, redirects to the products page.

- Otherwise, displays the checkout form.

``class CheckoutView.post():``

- Validates the form and creates an ``Order`` linked to the user.

- Saves each bag item as an ``OrderLineItem.``

- Builds Stripe line items, including delivery cost if needed.

- Creates a Stripe Checkout Session and redirects the user to payment.

- Empties the shopping bag in the session.
## checkout_success
**function** 🟩
```python
def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    ...
    return render(request, 'checkout/checkout_success.html', {'order': order})
```
**urls** 🟩
```python
urlpatterns = [
    path('success/<order_number>/', checkout_success, name='checkout_success'),
]
```
**html** 🟧 **Jinja** ⬜
``pixel-store/checkout/templates/checkout/checkout_success.html``
```html
<p>Your order number is: <strong>{{ order.order_number }}</strong></p>
    <a href="{% url 'my_orders' %}" class="checkout-button continue-btn mb-2">View My Orders</a><br>
    <a href="{% url 'products_list' %}" class="checkout-button continue-btn ">Continue shopping</a>
```
``checkout_success():``

- Finds the completed order.

- Clears the session bag and deletes DB ``BagItem`` for the user.

- Shows a success message and the confirmation page.
## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
