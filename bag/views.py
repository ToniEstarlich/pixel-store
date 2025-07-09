from django.shortcuts import redirect, render
from django.http import JsonResponse
from .context_processors import bag_contents, calculate_bag_total
from django.views.decorators.http import require_POST
from products.models import Product
from .models import BagItem

def view_bag(request):
    bag = request.session.get('bag', {})
    bag_items = []

    for item_key, quantity in bag.items():
        try:
            item_id, size = item_key.split('_')
            product = Product.objects.get(pk=int(item_id))
        except (Product.DoesNotExist, ValueError):
            continue

        subtotal = product.price * quantity

        bag_items.append({
            'item_id': item_id,
            'product': product,
            'quantity': quantity,
            'size': size,
            'subtotal': subtotal,
        })

    # calculate the cost of send
    total = calculate_bag_total(bag)
    delivery_cost = 5  if total <50 else 0
    grand_total = total + delivery_cost

    context = {
        'bag_items': bag_items,
        'grand_total': calculate_bag_total(bag),
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
    }

    return render(request, 'bag/bag.html', context)

def add_to_bag(request, item_id):
    size = request.POST.get('size')
    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})
    key = f'{item_id}_{size}'

    if key in bag:
        bag[key] += quantity
    else:
        bag[key] = quantity

    request.session['bag'] = bag

    if request.user.is_authenticated:
        product = Product.objects.get(pk=item_id)
        bag_item, created = BagItem.objects.get_or_create(
            user=request.user,
            product=product,
            size=size,
            defaults={'quantity': quantity}
        )
        if not created:
            bag_item.quantity += quantity
            bag_item.save()

    grand_total = calculate_bag_total(bag)

    return JsonResponse({
        'message': 'Product added to bag',
        'grand_total': f'{grand_total:.2f}'
    })

@require_POST
def remove_from_bag(request, item_id):
    size = request.POST.get('size')
    key = f'{item_id}_{size}'
    bag = request.session.get('bag', {})

    if key in bag:
        del bag[key]
        request.session['bag'] = bag

    if request.user.is_authenticated:
       BagItem.objects.filter(
         user=request.user,
         product_id=item_id,
         size=size
       ).delete()

    return redirect('view_bag')


def clear_bag(request):
    request.session['bag'] = {}

    if request.user.is_authenticated:
        BagItem.objects.filter(user=request.user).delete()
        
    return redirect('view_bag')

