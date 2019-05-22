from django.db.models import Sum

from bobs_banana_stand.celery import app
from bobs_banana_stand.redis.product_stock_management import ProductStockManagement
from metrics.models import InventoryProduct
from product.models.product import Product
from purchasing.models import PurchasedOrder
from sales.models import SalesOrder


@app.task
def generate_inventory_products():
    for product in Product.objects.all():
        purchased_order = PurchasedOrder.objects.filter(product=product)
        total_qty_purchased = purchased_order.aggregate(Sum('quantity')).get('quantity__sum')
        total_qty_sold = SalesOrder.objects.filter(product=product).aggregate(Sum('quantity')).get('quantity__sum')
        total_qty_expired = purchased_order.filter(expired=True).aggregate(Sum('quantity')).get('quantity__sum')
        total_qty_in_stock = sum(ProductStockManagement(purchased_order.first()).stock.values())
        profit = (total_qty_sold * product.unit_price) - (total_qty_purchased * product.unit_cost)

        InventoryProduct.objects.create(
            product=product,
            total_qty_purchased=total_qty_purchased,
            total_qty_sold=total_qty_sold,
            total_qty_expired=total_qty_expired,
            total_qty_in_stock=total_qty_in_stock,
            profit=profit
        )
