from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register, name='register'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('profile/edit/', views.profile_view, name='edit_profile'),
]