from bobs_banana_stand.redis.product_stock_management import ProductStockManagement


class Signals(object):
    @staticmethod
    def create_or_update_order_stock(instance, **kwargs):
        print('create or update order stock gets called')
        ProductStockManagement(instance).create_or_update_order_stock()

    @staticmethod
    def update_redis_stock(instance, **kwargs):
        ProductStockManagement(instance).update_overall_stock()

    @staticmethod
    def decrease_order_stock(instance, **kwargs):
        ProductStockManagement(instance).decrease_order_stock()

    @staticmethod
    def verify_sold_out_purchased_orders(instance, **kwargs):
        from purchasing.models import PurchasedOrder

        stock = ProductStockManagement(instance).stock

        for purchased_product_id, quantity in stock.items():
            if quantity == 0:
                PurchasedOrder.objects.filter(id=purchased_product_id).update(sold_out=True)
