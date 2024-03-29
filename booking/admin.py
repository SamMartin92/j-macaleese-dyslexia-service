from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('user', 'booking_date', 'status')
    list_display = (
        'user',
        'booking_type',
        'booking_date',
        'time_slot',
        'status')

