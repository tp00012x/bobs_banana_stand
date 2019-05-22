from django.db import models

from product.models.product import Product
from sales.models import SalesOrder


# TODO I might rename this table to make more sense as this will be the generated record when I choose a start and end
#  date
class InventoryProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    total_qty_purchased = models.IntegerField(default=0)  # sum of all purchased orders' quantity for this product
    total_qty_sold = models.IntegerField(default=0)  # sum of all Sales Orders' quantities for this product
    total_qty_expired = models.IntegerField(default=0)  # calculated field based on purchased date for this product
    total_qty_in_stock = models.IntegerField(default=0)  # total_qty_purchased - total_qty_sold
    profit = models.FloatField(default=0.00)  # total_qty_sold * unit_price - total_qty_purchased * unit cost
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - Unit Price: {} - <{}> in stock'.format(self.product,
                                                            self.product.unit_price,
                                                            self.total_qty_in_stock)
