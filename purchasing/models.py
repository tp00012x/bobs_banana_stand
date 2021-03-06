from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save

from product.models.product import Product
from purchasing.services.models_logic import PurchasedOrderLogic
from purchasing.signals import PurchasedOrderSignals
from sales.models import SalesOrder


class PurchasedOrder(models.Model):
    original_quantity = None

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    in_stock = models.IntegerField()
    expired = models.BooleanField(default=False)  # if purchased date = time now - shelf life, this will be true
    sold_out = models.BooleanField(default=False)
    purchased_date = models.DateTimeField(auto_now_add=True)  # automatically generated
    updated_at = models.DateTimeField(auto_now=True)  # automatically generated

    def __init__(self, *args, **kwargs):
        super(PurchasedOrder, self).__init__(*args, **kwargs)
        self.original_quantity = self.quantity

    def save(self, *args, **kwargs):
        # Only run when purchased order is being updated
        if self.pk:
            PurchasedOrderLogic.run_validations(self, self.original_quantity)

        super(PurchasedOrder, self).save(*args, **kwargs), self.id
        self.original_quantity = self.quantity

    def delete(self, *args, **kwargs):
        PurchasedOrderLogic.run_validations(self, self.original_quantity)

        super(PurchasedOrder, self).delete(*args, **kwargs)

    def __str__(self):
        return "Product: {} ({}) - Quantity Purchased: {}".format(self.product.name, self.product.id, self.quantity)


pre_save.connect(PurchasedOrderSignals.update_in_stock_value, sender=PurchasedOrder)
post_save.connect(PurchasedOrderSignals.create_or_update_order_stock, sender=PurchasedOrder)
post_delete.connect(PurchasedOrderSignals.deletes_order_stock, sender=PurchasedOrder)
