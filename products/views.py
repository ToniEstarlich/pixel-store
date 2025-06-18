from django.shortcuts import render
from django.utils.timezone import now
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/products_list.html', {
        'products': products,
        'timestamp': now().timestamp()
    })

def search(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'products/search_results.html', {''
    'results': results, 
    'query': query,
    })
