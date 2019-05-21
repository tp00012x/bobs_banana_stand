from rest_framework import serializers

from product.models.supplier import Supplier


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = ('pk', 'name',)
