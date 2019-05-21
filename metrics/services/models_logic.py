class InventoryProductLogic(object):
    pass

    # def __init__(self, inventory_product, product_id):
    #     self.inventory_product = inventory_product
    #     self.product_id = product_id
    #     self.product = self.get_product()
    #
    # def update_inventory_product_fields(self):
    #     print('run update_inventory_product_fields')
    #     self._update_total_qty_in_stock()
    #     self._update_profit()
    #
    # def _update_total_qty_in_stock(self):
    #     from purchasing.models import PurchasedOrder
    #
    #     purchase_order = PurchasedOrder.objects.filter(product_id=self.product_id)
    #
    #     print(self.product_id)
    #     print(purchase_order)
    #
    #     total_qty_purchased = purchase_order.aggregate(Sum('qty_purchased')).get('qty_purchased__sum')
    #     total_qty_sold = purchase_order.aggregate(Sum('qty_sold')).get('qty_sold')
    #
    #     print(total_qty_purchased)
    #     print(total_qty_sold)
    #
    #     self.inventory_product.total_qty_in_stock = total_qty_purchased - total_qty_sold
    #     self.inventory_product.save(update_fields={'total_qty_in_stock'})
    #
    # def _update_profit(self):
    #     from sales.models import SalesOrder
    #
    #     sales_order = SalesOrder.objects.filter(inventory_product_id=self.inventory_product.id)
    #     total_order_purchase_cost = sales_order.aggregate(Sum('order_purchase_cost')).get('order_purchase_cost__sum')
    #     total_revenue_per_order = sales_order.aggregate(Sum('revenue_per_order')).get('revenue_per_order__sum')
    #
    #     print(total_order_purchase_cost)
    #     print(total_revenue_per_order)
    #
    #     self.inventory_product.profit = total_order_purchase_cost - total_revenue_per_order
    #     self.inventory_product.save(update_fields={'profit'})
    #
    # def get_product(self):
    #     try:
    #         product = Product.objects.get(pk=self.product_id)
    #     except Product.DoesNotExist:
    #         pass
    #     else:
    #         return product
