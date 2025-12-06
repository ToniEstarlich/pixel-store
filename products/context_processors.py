from .models import Category
from django.shortcuts import render


def get_categories(request):
    from .models import Category

    categories = Category.objects.all()
    return {"categories": categories}
