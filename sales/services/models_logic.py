from bobs_banana_stand.redis.product_stock_management import ProductStockManagement


class SalesOrderLogic(object):
    def __init__(self, sales_order):
        self.sales_order = sales_order
        self.stock = ProductStockManagement(self.sales_order).stock

    def update_purchased_order_stock(self):
        from purchasing.models import PurchasedOrder

        for purchased_order_id, stock in self.stock.items():
            # here is another example where the we need to do a field update in a non-elegant fashion to bypass the
            # save() method when using sqlite
            if self._get_purchased_order(purchased_order_id):
                PurchasedOrder.objects.filter(id=purchased_order_id).update(in_stock=stock)

    def validate_if_in_stock(self):
        if self.sales_order.quantity > sum(self.stock.values()):
            raise Exception('There is not enough in stock for product with id {}'.format(self.sales_order.product.id))

    @staticmethod
    def _get_purchased_order(purchased_order_id):
        from purchasing.models import PurchasedOrder

        try:
            PurchasedOrder.objects.get(id=purchased_order_id)
        except PurchasedOrder.DoesNotExist:
            return False
        else:
            return True
