from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import BagItem


@receiver(user_logged_in)
def load_bag_from_db(sender, request, user, **kwargs):
    bag = {}
    for item in BagItem.objects.filter(user=user):
        key = f"{item.product.id}_{item.size}"
        bag[key] = item.quantity
    request.session["bag"] = bag
