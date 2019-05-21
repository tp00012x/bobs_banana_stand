from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save

from bobs_banana_stand.redis.product_stock_management import ProductStockManagement
from bobs_banana_stand.signals import Signals
from product.models.product import Product

from sales.models import SalesOrder


class PurchasedOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    expired = models.BooleanField(default=False)  # if purchased date = time now - shelf life, this will be true
    sold_out = models.BooleanField(default=False)
    purchased_date = models.DateTimeField(auto_now_add=True)  # automatically generated
    updated_at = models.DateTimeField(auto_now=True)  # automatically generated

    def delete(self, *args, **kwargs):
        # We can't delete a purchased order that has already been sold or is in the process of being sold
        ProductStockManagement(self).validate_if_product_has_been_sold()

        super(PurchasedOrder, self).delete(*args, **kwargs)

    def __str__(self):
        return "Product: {} ({}) - Quantity Purchased: {}".format(self.product.name, self.product.id, self.quantity)


post_save.connect(Signals.create_or_update_order_stock, sender=PurchasedOrder)
post_delete.connect(Signals.decrease_order_stock, sender=PurchasedOrder)
