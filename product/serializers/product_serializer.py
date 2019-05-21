from rest_framework.serializers import HyperlinkedModelSerializer

from product.models.product import Product


class ProductSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'name', 'supplier', 'unit_price', 'unit_cost', 'shelf_life',)
