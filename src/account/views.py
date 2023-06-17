"""Auth App views."""

from rest_framework import generics, permissions

# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import status
from .serializers import CustomerSerializer

# Create your views here.


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


'''
    def put(self, request, *args, **kwargs):
        """Handle HTTP PUT request to update user information."""
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(
            {"message": "User information updated successfully."},
            status=status.HTTP_200_OK,
        )
'''
