from django.db import models

from product.models.supplier import Supplier


class Product(models.Model):
    BANANA = 'BAN'
    PRODUCT_CHOICES = (
        (BANANA, 'Banana'),
    )

    name = models.CharField(choices=PRODUCT_CHOICES, max_length=255, default=BANANA)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    unit_cost = models.DecimalField(max_digits=6, decimal_places=2)
    shelf_life = models.IntegerField(null=True, blank=True)  # The item might not expire
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ({})'.format(self.get_name_display(), self.pk)

