from rest_framework import viewsets, mixins

from purchasing.models import PurchasedOrder
from purchasing.serializers import PurchasedOrderSerializer


class PurchasedOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchasedOrder.objects.all()
    serializer_class = PurchasedOrderSerializer
