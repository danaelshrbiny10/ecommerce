"""Api App serializers."""

from rest_framework import serializers
from .models import Order, Product, CartItem


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
        fields = [
            "id",
            "product",
        ]


class OrderSerializer(serializers.ModelSerializer):
    """Order serializer class for order model."""

    product = ProductSerializer()

    class Meta:
        """Meta class."""

        model = Order
        fields = [
            "id",
            "product",
        ]


class CartItemCreateSerializer(serializers.Serializer):
    """Cart item serializer class for cart item model."""

    product = serializers.IntegerField(required=True)

    def validate_product(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError("This product is not avilable")
        return Product.objects.filter(pk=value).first()
