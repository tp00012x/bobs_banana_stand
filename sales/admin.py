from django.contrib import admin

from sales.models import SalesOrder


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(SalesOrder)
