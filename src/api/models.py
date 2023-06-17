"""API App models."""


from django.contrib.auth.models import User
from django.db import models
from core.models import TimeStampedModel


# Create your models here.


class Product(TimeStampedModel):
    """Product model."""

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    def __str__(self):
        """Override str method."""
        return self.name

    class Meta:
        """Meta class."""

        verbose_name = "Product"
        verbose_name_plural = "Products"


class CartItem(TimeStampedModel):
    """Cart item model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        """Override str method."""
        return f"{self.product.name} - {self.quantity}"

    class Meta:
        """Meta class."""

        verbose_name = "CartItem"
        verbose_name_plural = "CartItems"
