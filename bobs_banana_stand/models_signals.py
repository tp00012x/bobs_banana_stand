from bobs_banana_stand.redis.product_stock_management import ProductStockManagement


class ModelsSignals(object):
    @staticmethod
    def create_or_update_order_stock(instance, **kwargs):
        # We only want to create or update the stock for this purchased order if the following conditions are met
        if not instance.sold_out and not instance.expired:
            ProductStockManagement(instance).create_or_update_order_stock()

    @staticmethod
    def update_redis_stock(instance, **kwargs):
        ProductStockManagement(instance).update_overall_stock()

    @staticmethod
    def decrease_order_stock(instance, **kwargs):
        ProductStockManagement(instance).decrease_order_stock()

    @staticmethod
    def set_sold_out_purchased_orders(instance, **kwargs):
        from purchasing.models import PurchasedOrder

        stock = ProductStockManagement(instance).stock

        for purchased_product_id, quantity in stock.items():
            if quantity == 0:
                PurchasedOrder.objects.filter(id=purchased_product_id).update(sold_out=True)
