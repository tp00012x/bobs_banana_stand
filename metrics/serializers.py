from rest_framework import serializers

from metrics.models import InventoryProduct


class InventoryProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InventoryProduct
        fields = (
            'pk', 'product', 'total_qty_purchased', 'total_qty_sold', 'total_qty_expired', 'total_qty_in_stock',
            'profit',
        )
