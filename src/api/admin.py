"""API App admin."""


from django.contrib import admin
from .models import Product, CartItem


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin class for product model."""

    list_display = ("name", "price")
    fieldsets = (
        (
            "product Information",
            {
                "fields": ("price", "name"),
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
            },
        ),
    )


@admin.register(CartItem)
class CartItem(admin.ModelAdmin):
    """Admin class for CartItem model."""

    list_display = ("user", "product", "quantity")
    fieldsets = (
        (
            "CartItem Information",
            {
                "fields": ("user", "product", "quantity"),
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
            },
        ),
    )

    def has_add_permission(self, request):
        """Returns False to disable add permission."""
        return False

    def has_change_permission(self, request, obj=None):
        """Returns False to disable change permission."""
        return False

    def has_delete_permission(self, request, obj=None):
        """Returns False to disable delete permission."""
        return False
