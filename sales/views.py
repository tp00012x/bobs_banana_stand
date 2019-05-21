from rest_framework import viewsets, mixins

from sales.models import SalesOrder
from sales.serializers import SalesOrderSerializer


class SalesOrderViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
