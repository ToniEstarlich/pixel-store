def bag_contents(request):
    bag = request.session.get('bag', {})

    total = 0
    product_count = 0

    from products.models import Product 
    products = []
    for item_id, item_data in bag.items():
        product = Product.objects.get(id=item_id)
        quantity = item_data['quantity']
        total += product.price * quantity
        product_count += quantity
        products.append({
            'product': product,
            'quantity': quantity,
            'subtotal': product.price * quantity
        })

    context = {
        'bag_items': products,
        'grand_total': total,
        'product_count': product_count,
    }

    return context
