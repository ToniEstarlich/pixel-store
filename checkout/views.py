from django.shortcuts import render
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Order, OrderLineItem
from products.models import Product
from users.models import UserProfile
from .forms import OrderForm
from bag.context_processors import bag_contents
from django.contrib.auth.decorators import login_required
from bag.models import BagItem


# Stripe
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

class CheckoutView(View):
    def get(self, request):
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "Your bag is empty.")
            return redirect('products_list')
        
        form = OrderForm()
        return render(request, 'checkout/checkout.html', {'form': form})
    
    def post(self, request):
        bag = request.session.get('bag', {})
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            profile, _ = UserProfile.objects.get_or_create(user=request.user)
            order.user_profile = profile
            order.original_cart = bag
            order.save()

            if request.user.is_authenticated:
                order.user = request.user

            line_items = []
            for item_id, quantity in bag.items():
                product_id = int(item_id.split('_')[0])
                product = get_object_or_404(Product, pk=product_id)

                OrderLineItem.objects.create(order=order, product=product, quantity=quantity)

                line_items.append({ 
                    'price_data': {
                        'currency': 'gbp',
                        'product_data': {
                            'name': product.name,
                        },
                        'unit_amount': int(product.price * 100),
                        },
                    'quantity': quantity,
                })

            order.update_total()

            # calculate subtotal to bag
            total = sum(
                item['product'].price * item['quantity']
                for item in bag_contents(request)['bag_items']
            )
            delivery_cost = 500 if total < 50 else 0 
            grand_total = int(total * 100) + delivery_cost

            if delivery_cost > 0:
                 line_items.append({
                     'price_data': {
                         'currency': 'gbp',
                         'product_data': {
                             'name': 'Delivery Cost',
                        },
                      'unit_amount': delivery_cost,
                     },
                     'quantity': 1,
                })



            # Create Stripe Checkout:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=request.build_absolute_uri(
                    reverse('checkout_success', args=[order.order_number])
                ) + '?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=request.build_absolute_uri(
                    reverse('checkout')
                ),
            )

            request.session['bag'] = {} #this leave empty the bag
            return redirect(session.url, code=303)
        
        return render(request, 'checkout/checkout.html', {'form' : form})
    
def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    # Empty the bag after successful checkout
    if 'bag' in request.session:
        del request.session['bag']
        request.session.modified = True

    # clean the BagItems of basedate users
    BagItem.objects.filter(user=request.user).delete()

    messages.success(request, f'Order successfully processed! Your order number is {order_number}. A confirmation email will be sent to you.')

    return render(request, 'checkout/checkout_success.html', {'order': order})
