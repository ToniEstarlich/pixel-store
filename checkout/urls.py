from django.urls import path
from .views import CheckoutView, checkout_success

urlpatterns = [
    path("", CheckoutView.as_view(), name="checkout"),
    path("success/<order_number>/", checkout_success, name="checkout_success"),
]
