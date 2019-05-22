from rest_framework import viewsets

from purchasing.models import PurchasedOrder
from purchasing.serializers import PurchasedOrderSerializer


# we support the delete, update and save methods for purchased products.
class PurchasedOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchasedOrder.objects.all()
    serializer_class = PurchasedOrderSerializer
