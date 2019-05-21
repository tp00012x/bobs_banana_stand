from rest_framework import viewsets, mixins

from metrics.models import InventoryProduct
from metrics.serializers import InventoryProductSerializer

# todo uncomment this later
# class InventoryProductViewSet(mixins.ListModelMixin,
#                               mixins.RetrieveModelMixin,
#                               viewsets.GenericViewSet):
#     queryset = InventoryProduct.objects.all()
#     serializer_class = InventoryProductSerializer


class InventoryProductViewSet(viewsets.ModelViewSet):
    queryset = InventoryProduct.objects.all()
    serializer_class = InventoryProductSerializer

