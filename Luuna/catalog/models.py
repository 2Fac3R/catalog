from django.db import models

# Create your models here.

class Product(models.Model):
    """Model representing a Product"""
    sku = models.CharField('SKU', max_length=12, unique=True, 
        help_text = "A stock-keeping unit (SKU) is a scannable bar code, most often seen printed on product labels in a retail store.")
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    brand = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
