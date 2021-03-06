from rest_framework import serializers

from purchasing.models import PurchasedOrder


class PurchasedOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedOrder
        fields = ('pk', 'product', 'quantity', 'in_stock', 'sold_out', 'expired', 'purchased_date',)
        read_only_fields = ('in_stock', 'sold_out', 'expired',)

    def create(self, validated_data):
        return PurchasedOrder.objects.create(**validated_data)
