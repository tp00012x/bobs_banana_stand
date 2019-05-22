from bobs_banana_stand.redis.product_stock_management import ProductStockManagement


class PurchasedOrderSignals(object):
    @staticmethod
    def update_in_stock_value(instance, **kwargs):
        instance.in_stock = instance.quantity

    @staticmethod
    def create_or_update_order_stock(instance, **kwargs):
        # We only want to create or update the stock for this purchased order if the following conditions are met
        if not instance.sold_out and not instance.expired:
            ProductStockManagement(instance).create_or_update_order_stock()

    @staticmethod
    def decrease_order_stock(instance, **kwargs):
        ProductStockManagement(instance).decrease_order_stock()
