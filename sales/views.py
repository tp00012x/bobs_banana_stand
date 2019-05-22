from rest_framework import viewsets, mixins

from sales.models import SalesOrder
from sales.serializers import SalesOrderSerializer


# we are not going to support deletion for sales orders. Bananas go bad, they can't return biodegradable items :)
class SalesOrderViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
