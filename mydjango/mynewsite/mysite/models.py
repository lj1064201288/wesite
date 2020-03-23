from django.db import models

# Create your models here.
class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Mudium'),
        ('L', 'Large'),
    )

    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    sku = models.IntegerField()
    qty = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)


    def __str__(self):
        return self.name