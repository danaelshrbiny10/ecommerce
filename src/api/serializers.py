"""Api App serializers."""

from rest_framework import serializers
from .models import Product, CartItem
import re
from account.models import Customer


class ProductSerializer(serializers.ModelSerializer):
    """Product serializer class for product model."""

    class Meta:
        """Meta class."""

        model = Product
        fields = ["name", "price"]


class CartItemSerializer(serializers.ModelSerializer):
    """Cart item serializer class for cart item model."""

    product = ProductSerializer()

    class Meta:
        """Meta class."""

        model = CartItem
        fields = ["user", "product", "quantity"]

    def create(self, validated_data: dict) -> Customer:
        """Create customer."""
        cart_items_data = validated_data.pop("cart_items", [])
        customer = self._create_profile(validated_data=validated_data)
        return self._create_cart_items(customer, cart_items_data)

    def _create_cart_items(self, customer: Customer, cart_items_data: list) -> None:
        """Private method to create cart items."""
        for cart_item_data in cart_items_data:
            product_data = cart_item_data.pop("product", {})
            product = self._create_product(product_data)
            CartItem.objects.create(
                customer=customer, product=product, **cart_item_data
            )

    def _create_product(self, product_data: dict) -> Product:
        """Private method to create product."""
        return Product.objects.create(**product_data)
