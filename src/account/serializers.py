"""Auth App serializers."""

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import Customer
import re


class CustomerSerializer(serializers.Serializer):
    """Customer serializer class for customer model."""

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    username = serializers.CharField(
        max_length=10, required=True, validators=[UniqueValidator(User.objects.all())]
    )
    shipping_address = serializers.CharField(required=True)
    phone_number = serializers.CharField(
        required=True, validators=[UniqueValidator(Customer.objects.all())]
    )
    password = serializers.CharField(required=True)
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(User.objects.all())]
    )

    def validate_phone_number(self, value: str) -> str:
        """Validate phone number."""
        pattern = r"^\+20\d{10}$"
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Invalid phone number. The phone number should start with '+20' and be followed by 10 digits."
            )
        return value

    def validate_password(self, value: str) -> str:
        """Validate the length of a new password"""
        if len(value) < 8:
            raise serializers.ValidationError("Password is short.")
        return value

    def create(self, validated_data: dict) -> Customer:
        """Create customer."""
        return self._create_profile(validated_data=validated_data)

    def _create_user(self, validated_data: dict) -> User:
        """Private method to create user object."""
        return User.objects.create_user(
            username=validated_data.get("username"),
            password=validated_data.get("password"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            email=validated_data.get("email"),
        )

    def _create_profile(self, validated_data: dict) -> Customer:
        """Private method to create user profile object."""
        return Customer.objects.create(
            shipping_address=validated_data.get("shipping_address"),
            phone_number=validated_data.get("phone_number"),
            user=self._create_user(validated_data=validated_data),
        )
