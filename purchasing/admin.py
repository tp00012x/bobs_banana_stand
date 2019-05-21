from django.contrib import admin

from purchasing.models import PurchasedOrder


class PurchasedOrderAdmin(admin.ModelAdmin):
    readonly_fields = ['expiration_date']


admin.site.register(PurchasedOrder)
