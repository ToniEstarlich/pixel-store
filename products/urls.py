from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products_list'),
    path('search/', views.search, name='search'),
]