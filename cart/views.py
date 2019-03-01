from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """ Renders the cart contents page """
    # You don't need to pass in a dictionary of cart contents because that context is available everywhere (specified in settings.py)
    return render(request, "cart.html")
    
def add_to_cart(request, id):
    """ Add a quantity of the specified product to the cart """
    
    # The integer comes from the form on the product page
    quantity = int(request.POST.get('quantity'))
    
    # The cart comes from the session. It will either get the cart if one exists, or an empty dictionary
    cart = request.session.get('cart', {})
    # What actually gets added is a product id and a quantity
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    
    return redirect(reverse('index'))

def adjust_cart(request, id):
    """ Adjust the quantity of the specified product to the specified amount """
    
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    # Can only adjust if the quantity is greater than 0
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))