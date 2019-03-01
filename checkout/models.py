from django.db import models
from products.models import Product

# Create your models here.

class Order(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=50, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county_or_province = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    
    def __str__(self):
        # Return a summary of the order as a string
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
class OrderLineItem(models.Model):
    # This goes to the Order class you created above
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)