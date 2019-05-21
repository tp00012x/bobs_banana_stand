from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers

from product.views import SupplierViewSet, ProductViewSet
from purchasing.views import PurchasedOrderViewSet
from sales.views import SalesOrderViewSet
from metrics.views import InventoryProductViewSet

router = routers.DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'purchased_orders', PurchasedOrderViewSet)
router.register(r'sales_orders', SalesOrderViewSet)
router.register(r'inventory_products', InventoryProductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^', include(router.urls)),
]
