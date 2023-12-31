"""Auth App views."""

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from .serializers import CustomerSerializer


class RegistrationView(generics.CreateAPIView):
    """Registration view."""

    serializer_class = CustomerSerializer

    def post(self, request):
        """Send Http POST request."""
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(
            {"message": "User registered successfully."}, status=status.HTTP_201_CREATED
        )
