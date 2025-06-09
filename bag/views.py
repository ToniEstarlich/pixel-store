
from django.shortcuts import  redirect, get_object_or_404
from products.models import Product

def view_bag(request):
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    size = request.POST.get('size', None)

    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id]['quantity'] += quantity
    else:
        bag[item_id] = {'quantity': quantity, 'size': size}

    request.session['bag'] = bag
    return redirect('view_bag')

