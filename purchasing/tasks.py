from datetime import timedelta

# from django.db.models import F
from django.utils import timezone

from bobs_banana_stand.celery import app
from purchasing.models import PurchasedOrder


@app.task
def check_for_expired_products():
    """
    Loops over all purchased products daily and checks if any of these products are expired. If so, it will set
    the expired field to True
    """

    # This one line SQL query could find all the expired products and set their expired field to True, but it can't be
    # used with sqlite3. One additional benefit of this approach is that we can run the update method on the query set
    # causing the method .save() to not be called.
    # PurchasedOrder.objects.filter(
    #     sold_out=False,
    #     expired=False,
    #     purchased_date__lt=timezone.now() - timedelta(days=1) * F("product__shelf_life").update(expired=True)
    # )

    # Thus, we will be using this less efficient/elegant approach
    for purchase_order in PurchasedOrder.objects.filter(sold_out=False, expired=False):
        if purchase_order.purchase_date < timezone.now() - timedelta(days=purchase_order.product.shelf_life):
            purchase_order.expired = True
            purchase_order.save(update_fields={'expired'})
