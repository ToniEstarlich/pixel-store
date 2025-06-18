from django.shortcuts import render
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.contrib import messages

from .models import Order, OrderLineItem
from products.models import Product
from users.models import UserProfile
from .forms import OrderForm
from bag.context_processors import bag_contents


class CheckoutView(View):
    def get(self, request):
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "Your bag is empty.")
            return redirect('products_list')
        
        form = OrderForm()
        return render(request, 'checkout/checkout.html', {'form': form})
    
    def post(self, request):
        cart = request.session.get('cart', {})
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if form.is_valid():
                profile = UserProfile.objects.get(user=request.user)
                order.user_profile = profile
            order.original_cart = cart
            order.save()

            for item_id, quantity in cart.items():
                product = get_object_or_404(Product, pk=item_id)
                line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity,
                )
                line_item.save()

            request.session['cart'] = {} #this leave empty the bag
            return redirect(reverse('checkout_success', args=[order.order_number]))
        
        return render(request, 'checkout/checkout.html', {'form' : form})
    
def checkout_success(request, order_number):
     
     order = get_object_or_404(Order, order_number=order_number)

      # we leave empy the bag 
     if 'bag' in request.session:
       del request.session['bag']

     messages.success(request, f'Order successfully processe! Your order number is {order_number}. A confirmation email will sent to you')
     return render(request, 'checkout/checkout_success.html', {'order': order})

