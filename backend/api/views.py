from django.contrib.auth.models import User
from rest_framework import generics
from .models import Cab, Booking
from .serializers import CabSerializer, BookingSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class CabListCreate(generics.ListCreateAPIView):
    queryset = Cab.objects.all()
    serializer_class = CabSerializer
    permission_classes = [AllowAny]

class CabRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cab.objects.all()
    serializer_class = CabSerializer
    permission_classes = [IsAuthenticated]

class BookingListCreate(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
