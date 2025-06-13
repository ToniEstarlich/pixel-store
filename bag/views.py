from django.shortcuts import redirect, render


def view_bag(request):
    return render(request, 'bag/bag.html')

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
    print("SESSION BAG:", request.session.get('bag', {}))
    return redirect('view_bag')

def clear_bag(request):
    request.session['bag'] = {}
    return redirect('add_to_bag_confirmation')

    # end of add to bag metod
   # return render(request, 'bag/bag.html')
