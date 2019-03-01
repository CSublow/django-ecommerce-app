from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    # Return all of the products that are in the database
    products = Product.objects.all()
    # Within products.html you will have access to all of the products
    return render(request, "products.html", {"products": products})