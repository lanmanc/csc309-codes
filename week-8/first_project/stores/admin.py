from django.contrib import admin

from stores.models import Store, Product


class ProductInline(admin.TabularInline):
    model = Product
    fields = ['name', 'price']


class StoreAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'url']
    fields = ['id', 'name', 'url']
    list_display = ['id', 'name', 'url']
    inlines = [ProductInline]


admin.site.register(Store, StoreAdmin)
admin.site.register(Product)
