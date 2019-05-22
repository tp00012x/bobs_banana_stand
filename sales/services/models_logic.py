from bobs_banana_stand.redis.product_stock_management import ProductStockManagement


class SalesOrderLogic(object):
    @staticmethod
    def update_purchased_order_stock(sales_order):
        from purchasing.models import PurchasedOrder

        stock = ProductStockManagement(sales_order).stock

        for purchase_order, stock in stock.items():
            # here is another example where the we need to do a field update in a non-elegant fashion to bypass the
            # save() method
            purchase_order = PurchasedOrder.objects.get(id=purchase_order)
            PurchasedOrder.objects.filter(id=purchase_order.id).update(in_stock=stock)

    @staticmethod
    def validate_if_in_stock(sales_order):
        stock = ProductStockManagement(sales_order).stock

        if sales_order.quantity > sum(stock.values()):
            raise Exception('There is not enough in stock for product with id {}'.format(sales_order.product.id))
