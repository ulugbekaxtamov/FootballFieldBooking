from datetime import timedelta
from django.utils import timezone

from rest_framework import serializers
from apps.booking.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'booking_number', 'user', 'football_field', 'start_time', 'end_time', 'total_price']

    def validate(self, data):
        data = super().validate(data)

        if data['end_time'] - data['start_time'] < timedelta(hours=1):
            raise serializers.ValidationError("Bookings must be at least 1 hour long.")

        if data['start_time'] < timezone.now():
            raise serializers.ValidationError("Bookings cannot be scheduled for previous dates.")

        busy = Booking.objects.filter(
            football_field=data['football_field'], start_time__lt=data['end_time'], end_time__gt=data['start_time']
        ).exists()
        if busy:
            raise serializers.ValidationError("This time period has already been booked.")

        return data
