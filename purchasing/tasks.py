from bobs_banana_stand.celery import app

from purchasing.services.models_logic import PurchasedOrderLogic


@app.task
def discard_expired_products():
    """
    Queries daily for all purchased products and checks if any of these products are expired. If so, it will set
    the expired field to True
    """
    PurchasedOrderLogic.find_and_update_expired_purchased_orders()
