from decimal import Decimal
from django.conf import settings
from products.models import Product


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get("bag", {})

    for item_key, quantity in bag.items():
        try:
            item_id, size = item_key.split("_")
            product = Product.objects.get(pk=int(item_id))
        except (Product.DoesNotExist, ValueError):
            continue

        subtotal = product.price * quantity
        total += subtotal
        product_count += quantity

        bag_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "product": product,
                "size": size,
                "subtotal": subtotal,
            }
        )

    grand_total = total

    return {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "grand_total": grand_total,
    }


def calculate_bag_total(bag):
    total = 0
    for item_key, quantity in bag.items():
        try:
            item_id, size = item_key.split("_")
            product = Product.objects.get(pk=int(item_id))
        except (Product.DoesNotExist, ValueError):
            continue
        total += product.price * quantity
    return total
