from django.contrib import admin

from .models import Category, Product

# log admin
# pas admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "category",
    )
    search_fields = (
        "name",
        "description",
    )
    list_filter = ("category",)
