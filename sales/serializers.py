from rest_framework import serializers

from sales.models import SalesOrder


class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ('pk', 'product', 'quantity', 'sold_date')

    def create(self, validated_data):
        return SalesOrder.objects.create(**validated_data)
