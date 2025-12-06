from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_bag, name="view_bag"),
    path("add/<int:item_id>/", views.add_to_bag, name="add_to_bag"),
    path("bag/remove/<item_id>", views.remove_from_bag, name="remove_from_bag"),
    path("clear/", views.clear_bag, name="clear_bag"),
]
