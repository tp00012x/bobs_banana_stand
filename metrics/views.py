from rest_framework import viewsets, mixins, filters

from metrics.models import InventoryProduct
from metrics.serializers import InventoryProductSerializer


class InventoryProductViewSet(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    queryset = InventoryProduct.objects.all()
    serializer_class = InventoryProductSerializer
    # filter_fields = ('created_date',)
