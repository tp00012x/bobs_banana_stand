from bobs_banana_stand.redis.product_stock_management import ProductStockManagement


class PurchasedOrderSignals(object):
    @staticmethod
    def update_in_stock_value(instance, **kwargs):
        # before save, we set the in_stock value to the quantity
        instance.in_stock = instance.quantity

    @staticmethod
    def create_or_update_order_stock(instance, **kwargs):
        # We only want to create or update the stock for this purchased order if the following conditions are met
        if not instance.sold_out and not instance.expired:
            ProductStockManagement(instance).create_or_update_order_stock()

    @staticmethod
    def deletes_order_stock(instance, **kwargs):
        # if the purchased order is deleted, we want to set the stock to 0
        ProductStockManagement(instance).deletes_order_stock()
