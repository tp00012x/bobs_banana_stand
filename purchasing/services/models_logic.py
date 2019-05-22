from bobs_banana_stand.redis.product_stock_management import ProductStockManagement


class PurchasedOrderLogic(object):
    @classmethod
    def run_validations(cls, purchased_order, original_quantity):
        cls._check_if_expired(purchased_order)
        cls._check_if_sold_out(purchased_order)
        cls._validate_if_product_is_being_sold(purchased_order, original_quantity)

    @staticmethod
    def _check_if_expired(purchased_order):
        """
        Check if the purchased order has expired
        """
        if purchased_order.expired:
            raise Exception(
                "You can't perform the following action because the purchased order with id: {} is expired".format(
                    purchased_order.id
                )
            )

    @staticmethod
    def _check_if_sold_out(purchased_order):
        """
          Check if the purchased order is sold out
        """
        if purchased_order.sold_out:
            raise Exception(
                "You can't perform the following action because the purchased order with id: {} has already been "
                "sold".format(purchased_order.id)
            )

    @staticmethod
    def _validate_if_product_is_being_sold(purchased_order, original_quantity):
        """
          Check if the purchased order is on the process of being sold
        """
        stock = ProductStockManagement(purchased_order).stock

        if original_quantity != stock.get(str(purchased_order.id)):
            raise Exception(
                "You can't perform the following action because this order with id: {} is in the process of being "
                "sold".format(purchased_order.id)
            )
