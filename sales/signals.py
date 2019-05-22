from bobs_banana_stand.redis.product_stock_management import ProductStockManagement


class SalesOrdersSignals(object):
    @staticmethod
    def update_redis_stock(instance, **kwargs):
        ProductStockManagement(instance).update_overall_stock()

    @staticmethod
    def set_sold_out_purchased_orders(instance, **kwargs):
        from purchasing.models import PurchasedOrder

        stock = ProductStockManagement(instance).stock

        for purchased_product_id, quantity in stock.items():
            if quantity == 0:
                PurchasedOrder.objects.filter(id=purchased_product_id).update(sold_out=True)
