from django.contrib import admin
from django.utils import timezone
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking_number', 'user', 'football_field', 'start_time', 'end_time', 'total_price')
    search_fields = ('booking_number', 'user__username', 'football_field__name')
    list_filter = ('football_field', 'start_time', 'end_time')
    readonly_fields = ('total_price', 'booking_number')
    date_hierarchy = 'start_time'

    def has_change_permission(self, request, obj=None):
        if obj and obj.start_time <= timezone.now():
            return False
        return super().has_change_permission(request, obj)

    def get_queryset(self, request):
        return Booking.all_objects.all()
