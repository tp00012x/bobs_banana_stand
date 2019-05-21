from django.db import models
from django.db.models.signals import post_save, post_delete

from bobs_banana_stand.redis.product_stock_management import ProductStockManagement
from bobs_banana_stand.signals import Signals
from product.models.product import Product
from sales.tasks import place_order


class SalesOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sold_date = models.DateTimeField(auto_now_add=True)  # automatically generated
    updated_at = models.DateTimeField(auto_now=True)  # automatically generated

    def save(self, *args, **kwargs):
        # verify that order can be completed by checking if there is enough in stock for this product
        ProductStockManagement(self).validate_if_in_stock()

        # places order by adding it to the celery queue to support FIFO policy
        place_order.delay(super(SalesOrder, self).save(*args, **kwargs), self.id)

    def __str__(self):
        return "Product: {} ({}) - Quantity Sold: {}".format(self.product.name, self.product.id, self.quantity)


post_save.connect(Signals.update_redis_stock, sender=SalesOrder)
post_save.connect(Signals.verify_sold_out_purchased_orders, sender=SalesOrder)

