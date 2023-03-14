from django.contrib import admin

from webapp.models import Product, Cart


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "category",
        "price",
        "image",
        "balance",
    )
    list_filter = (
        "id",
        "title",
        "description",
        "category",
        "price",
        "image",
        "balance",
    )
    search_fields = ("title", "description", "category", "price", "balance")
    fields = ("title", "description", "category", "price", "image", "balance")
    readonly_fields = ("id", "created_at", "updated_at")


admin.site.register(Product, ProductAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "balance",
    )
    list_filter = ("id", "balance",)
    search_fields = ("product", "balance",)
    fields = (
        "product",
        "balance",
    )
    readonly_fields = ("id",)


admin.site.register(Cart, CartAdmin)