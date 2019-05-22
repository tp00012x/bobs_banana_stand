from datetime import timedelta

# from django.db.models import F
from django.utils import timezone

from bobs_banana_stand.celery import app
from purchasing.models import PurchasedOrder


@app.task
def check_for_expired_products():
    print('check for expired products')
    # This one line SQL query could find all the expired products, but it can't be used with sqlite3
    # PurchasedOrder.objects.filter(
    #     sold_out=False,
    #     expired=False,
    #     purchased_date__lt=timezone.now() - timedelta(days=1) * F("product__shelf_life").update(expired=True)
    # )

    # Thus, we will be using this less elegant approach
    for purchase_order in PurchasedOrder.objects.filter(sold_out=False, expired=False):
        if purchase_order.purchase_date < timezone.now() - timedelta(days=purchase_order.product.shelf_life):
            purchase_order.expired = True
            purchase_order.save(update_fields={'expired'})
