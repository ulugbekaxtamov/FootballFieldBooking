from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from apps.base.models import Base
from apps.football_field.models import FootballField
from apps.user.models import User

from decimal import Decimal


class Booking(Base):
    booking_number = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    football_field = models.ForeignKey(FootballField, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    total_price = models.DecimalField(default=0, decimal_places=2, max_digits=10, editable=False)

    def save(self, *args, **kwargs):
        if self.start_time >= self.end_time:
            raise ValidationError("Start time must be before end time")
        if self.start_time < timezone.now():
            raise ValidationError("Start time must be in the future")

        duration = Decimal((self.end_time - self.start_time).total_seconds()) / Decimal(3600)
        self.total_price = duration * Decimal(self.football_field.price_per_hour)

        if not self.booking_number:
            last_booking = Booking.objects.filter(
                football_field=self.football_field).order_by('-booking_number').first()
            if last_booking:
                self.booking_number = last_booking.booking_number + 1
            else:
                self.booking_number = 1

        super().save(*args, **kwargs)
