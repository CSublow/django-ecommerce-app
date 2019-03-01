from django.shortcuts import get_object_or_404
from products.models import Product
    
def cart_contents(request):
    """ Ensures that the cart contents are available when rendering every page within the project """
    
    # Request the existing cart if there is one or a blank dictionary if there is not
    cart = request.session.get('cart', {})
    
    # Initialize cart_items, total and product count
    cart_items = []
    total = 0
    product_count = 0
    
    # The id is product id, the quantity how many the user wishes to purchase
    for id, quantity in cart.items():
        # product comes from the product model
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
        
    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count }
        