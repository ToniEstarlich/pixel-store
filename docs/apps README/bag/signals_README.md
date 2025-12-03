## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)
# pixel-store/bag/apps.py
"Signals automatically execute functions in response to model events and are activated by importing them in the app’s ``apps.py``, not via URLs or ``settings.py``."

**app**🟦
```python
class BagConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'

    def ready(self):
        import bag.signals
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
# pixel-store/bag/signals.py
## load_bag_from_db
**function** 🟩
```python
@receiver(user_logged_in)
def load_bag_from_db(sender, request, user, **kwargs):
    bag = {}
    for item in BagItem.objects.filter(user=user):
        key = f"{item.product.id}_{item.size}"
        bag[key] = item.quantity
    request.session['bag'] = bag
```

``load_bag_from_db:``

- Runs when a user logs in.

- Loads all ``BagItem`` records belonging to that user from the database.

- Rebuilds the session bag using the product ID and size as the key.

- Stores this reconstructed bag in ``request.session['bag'].``
## Comeback [README](../../../README.md#the-functions-and-their-testing-on-the-pixel-store-app)