from django.contrib import admin

from metrics.models import InventoryProduct


class InventoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(InventoryProduct)
