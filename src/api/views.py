"""API App views."""

from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from .serializers import ProductSerializer, CartItemSerializer
from .models import Product, CartItem
# Create your views here.

class ProductListItems(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    """View to list all products."""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


    def get(self, request, *args, **kwargs):
        """GET items."""
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Update items."""
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """POST items."""
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete items."""
        return self.destroy(request, *args, **kwargs)
    

class CartListItems(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    """View to create a cart item."""
    serializer_class = CartItem
    queryset = CartItem.objects.all()


    def get(self, request, *args, **kwargs):
        """GET items."""
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Update items."""
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """POST items."""
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete items."""
        return self.destroy(request, *args, **kwargs)