from bobs_banana_stand.redis.product_stock_management import ProductStockManagement


class SalesOrderLogic(object):
    @staticmethod
    def validate_if_in_stock(sales_order):
        stock = ProductStockManagement(sales_order).stock

        if sales_order.quantity > sum(stock.values()):
            raise Exception('There is not enough in stock for product with id {}'.format(sales_order.product.id))
