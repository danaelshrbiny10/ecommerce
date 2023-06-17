"""Auth App admin."""

from django.contrib import admin
from . models import Customer

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Admin class for customer model."""

    
    list_display = ("user", "phone_number")
    fieldsets = (
        (
            "customer Information",
            {
                "fields": ("user", "phone_number","shipping_address"),
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