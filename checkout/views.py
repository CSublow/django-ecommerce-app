from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required # You want your customer to be logged in when they go to the checkout
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# The views here require the api keys from stripe. These were set in settings.py
stripe.api_key = settings.STRIPE_SECRET

# Within this view the user is given the orderform to fill out
@login_required()
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date= timezone.now()
            order.save()
            
            # You can get the information about what has been purchased from the cart
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = quantity
                    )
                order_line_item.save()
                
                try:
                    customer = stripe.Charge.create(
                        amount = int(total * 100), # Stripe uses everything in decimals, so £10 would be 1000
                        currency = "EUR",
                        description = request.user.email, # So you can see who the payment came from in the stripe dashboard
                        card = payment_form.cleaned_data['stripe_id'])
                
                # For if the card is declined   
                except stripe.error.CardError:
                    messages.error(request, "Your card was declined!")
                    
                # If the customer has successfully paid, take them back to the products page
                if customer.paid:
                    messages.error(request, "You have successfully paid")
                    request.session['cart'] = {}
                    return redirect(reverse('products'))
                else:
                    messages.error(request, "Unable to take payment")
                
        else:
            print(payment_form.errors)
            messages.error(request, "We are unable to take payment with that card!")
                
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
                
    # Send the user to checkout.html, include the order form, payment form and publishable (whatever that is)
    return render(request, "checkout.html", {"order_form": order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})