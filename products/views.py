from django.shortcuts import render
from django.utils.timezone import now
from .models import Product
from .models import Product, Category

def product_list(request):
    category_name = request.GET.get('category')

    if category_name:
        products = Product.objects.filter(category__name=category_name)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()

    return render(request, 'products/products_list.html', {
        'products': products,
        'categories': categories,
        'timestamp': now().timestamp(),
        'selected_category': category_name,
    })

def search(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'products/search_results.html', {''
    'results': results, 
    'query': query,
    })