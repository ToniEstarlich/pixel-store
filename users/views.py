from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm, UserForm
from .forms import CustomRegisterForm
from django.contrib.auth import login
from checkout.models import Order


def register(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # create register
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect("profile")
        else:
            form = CustomRegisterForm()
        return render(request, "users/register.html", {"form": form})


@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)

    return render(
        request,
        "users/profile.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
        },
    )


@login_required
def my_orders(request):

    user_profile = UserProfile.objects.get(user=request.user)

    orders = Order.objects.filter(user_profile=user_profile).order_by("-date")

    return render(request, "users/my_orders.html", {"orders": orders})
