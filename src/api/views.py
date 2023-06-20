"""API App views."""
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from account.models import Customer
from .serializers import (
    CartItemCreateSerializer,
    OrderSerializer,
    ProductSerializer,
    CartItemSerializer,
)
from .models import Order, Product, CartItem
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class ProductListView(mixins.ListModelMixin, GenericAPIView):
    """View to list all products."""

    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('price')
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Override get queryset method."""
        name = self.request.query_params.get("name", None)
        if name is not None:
            return self.queryset.filter(name__icontains=name)
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        """send GET request."""
        return self.list(request, *args, **kwargs)


class ProductSingleItemView(mixins.RetrieveModelMixin, GenericAPIView):
    """View to list all products."""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """send GET request."""
        return self.retrieve(request, *args, **kwargs)


class CardItemView(
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    """View to list all user cart items."""

    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Override get queryset method."""
        customer = Customer.objects.get(user=self.request.user)
        return self.queryset.filter(user=customer)

    def get(self, request, *args, **kwargs):
        """send GET request."""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Overide the post method."""
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Overide the delete method."""
        return self.destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Override the create method."""
        serializer = CartItemCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        customer = Customer.objects.get(user=self.request.user)
        CartItem.objects.create(
            user=customer, product=serializer.validated_data.get("product")
        )
        return Response(
            {"message": "Item added to cart successfully."}, status=status.HTTP_200_OK
        )


class OrderView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    """View to list all user order items."""

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Override get queryset method."""
        customer = Customer.objects.get(user=self.request.user)
        return self.queryset.filter(user=customer)

    def get(self, request, *args, **kwargs):
        """send GET request."""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Overide the post method."""
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Override the create method."""
        customer = Customer.objects.get(user=self.request.user)
        Order.from_cart_to_order(customer=customer)
        return Response(
            {"message": "Order Created successfully."}, status=status.HTTP_200_OK
        )
