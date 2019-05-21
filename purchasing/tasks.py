from datetime import timedelta

from django.db.models import F
from django.utils import timezone

from bobs_banana_stand.celery import app
from purchasing.models import PurchasedOrder


@app.task
def check_for_expired_products():
    print('check for expired products')
    PurchasedOrder.objects.filter(
        expired=False,
        purchased_date__lt=timezone.now() - timedelta(days=10) * F("product__shelf_life"),
    )
