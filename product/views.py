from rest_framework import viewsets

from product.models.product import Product, Supplier
from product.serializers.product_serializer import ProductSerializer
from product.serializers.supplier_serializer import SupplierSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
