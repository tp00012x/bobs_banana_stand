from django.contrib import admin

from product.models.product import Product, Supplier


class ProductAdmin(admin.ModelAdmin):
    pass


class SupplierAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product)

admin.site.register(Supplier)
