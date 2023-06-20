"""Api App urls."""

from django.urls import include, path
from .views import (
    ProductListView,
    ProductSingleItemView,
    CardItemView,
    OrderView,
)


urlpatterns = [
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductSingleItemView.as_view(), name="product-detail"),
    path("cart/", CardItemView.as_view(), name="cart"),
    path("cart/<int:pk>/", CardItemView.as_view(), name="cart-delete"),
    path("order/", OrderView.as_view(), name="order"),
]
