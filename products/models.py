from django.db import models

# Create your models here.
class Product(models.Model):
    # By default the product name is empty
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # Images will be uploaded to a directory called images
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name
    