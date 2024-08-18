from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from apps.booking.models import Booking
from apps.user.models import User
from .serializers import BookingSerializer


class BookingListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer

    def get_queryset(self):
        user = self.request.user
        admin_group = Group.objects.get(name='Admin')
        owner_group = Group.objects.get(name='Owner')

        if User.objects.filter(groups=admin_group, id=user.id).exists():
            return Booking.objects.all()
        elif User.objects.filter(groups=owner_group, id=user.id).exists():
            return Booking.objects.filter(football_field__owner=user)
        else:
            return Booking.objects.filter(user=user)


class BookingCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user
        admin_group = Group.objects.get(name='Admin')
        owner_group = Group.objects.get(name='Owner')

        if User.objects.filter(groups=admin_group, id=user.id).exists():
            return Booking.objects.all()
        elif User.objects.filter(groups=owner_group, id=user.id).exists():
            return Booking.objects.filter(football_field__owner=user)
        else:
            return Booking.objects.filter(user=user)
