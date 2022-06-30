from django.contrib import admin
from .models import Booking
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('user', 'booking_date')
    list_display = ('user', 'booking_type', 'booking_date', 'time_slot')
