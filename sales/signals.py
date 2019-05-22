from bobs_banana_stand.redis.product_stock_management import ProductStockManagement
from sales.services.models_logic import SalesOrderLogic


class SalesOrdersSignals(object):
    @staticmethod
    def update_purchased_order_stock(instance, **kwargs):
        ProductStockManagement(instance).update_redis_stock()
        SalesOrderLogic(instance).update_purchased_order_stock()

    @staticmethod
    def set_sold_out_purchased_orders(instance, **kwargs):
        from purchasing.models import PurchasedOrder

        stock = ProductStockManagement(instance).stock

        for purchased_product_id, quantity in stock.items():
            if quantity == 0:
                PurchasedOrder.objects.filter(id=purchased_product_id).update(sold_out=True)
