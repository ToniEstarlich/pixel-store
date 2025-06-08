from django.shortcuts import render
from django.utils.timezone import now
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/products_list.html', {
        'products': products,
        'timestamp': now().timestamp()
    })
