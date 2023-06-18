"""API App models."""



from django.db import models
from account.models import Customer
from core.models import TimeStampedModel





class Product(TimeStampedModel):
    """Product model."""

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    def __str__(self) -> str:
        """Override str method."""
        return self.name

    class Meta:
        """Meta class."""

        verbose_name = "Product"
        verbose_name_plural = "Products"


class CartItem(TimeStampedModel):
    """Cart item model."""

    user = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self) -> str:
        """Override str method."""
        return f"{self.product.name} - {self.user.user.username}"

    class Meta:
        """Meta class."""

        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"


class Order(TimeStampedModel):
    """Ordered Items model"""

    user = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self) -> str:
        """Override str method."""
        return f"{self.product.name} - {self.user.user.username}"

    @classmethod
    def from_cart_to_order(cls, customer):
        """Transfare items from cart to product."""
        cart_items = CartItem.objects.filter(user=customer)
        for items in cart_items:
            cls.objects.create(
                user=customer,
                product=items.product
            )
        cart_items.delete()

    class Meta:
        """Meta class."""

        verbose_name = "Order"
        verbose_name_plural = "Orders"
