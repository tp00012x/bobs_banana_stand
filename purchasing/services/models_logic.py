from datetime import timedelta

from django.utils import timezone

from bobs_banana_stand.redis.product_stock_management import ProductStockManagement


class PurchasedOrderLogic(object):
    @classmethod
    def run_validations(cls, purchased_order, original_quantity):
        cls._check_if_expired(purchased_order)
        cls._check_if_sold_out(purchased_order)
        cls._validate_if_product_is_being_sold(purchased_order, original_quantity)

    @staticmethod
    def find_and_update_expired_purchased_orders():
        from purchasing.models import PurchasedOrder

        # This one line SQL query could find all the expired products and set their expired field to True, but it can't
        # be used with sqlite3. One additional benefit of this approach is that we can run the update method on the
        # query set causing the method .save() to never be called.
        # PurchasedOrder.objects.filter(
        #     sold_out=False,
        #     expired=False,
        #     purchased_date__lt=timezone.now() - timedelta(days=1) * F("product__shelf_life").update(expired=True)
        # )

        # Thus, we will be using this less efficient/elegant approach to do the same thing
        for purchased_order in PurchasedOrder.objects.filter(sold_out=False, expired=False):
            if purchased_order.purchased_date < timezone.now() - timedelta(minutes=1):
                PurchasedOrder.objects.filter(id=purchased_order.id).update(expired=True)
                # sets the stock for this purchased order to 0
                ProductStockManagement(purchased_order).deletes_order_stock()

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
