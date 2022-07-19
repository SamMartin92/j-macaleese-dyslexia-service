from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('class_type', 'booking_type', 'booking_date',
                  'time_slot',)
    