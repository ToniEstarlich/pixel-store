from django.db import models
from django.contrib.auth.models import User
from products.models import Product

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
