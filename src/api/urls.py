"""Api App urls."""

from django.urls import path
from .views import ProductListItems,CartListItems


urlpatterns = [
    path('product/', ProductListItems.as_view(), name='Product'),
    path('CartItem/', CartListItems.as_view(), name='Cart Item')
]