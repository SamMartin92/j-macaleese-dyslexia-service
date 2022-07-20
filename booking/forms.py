from django import forms
from django.forms.widgets import NumberInput
from .models import Booking

class BookingForm(forms.ModelForm):

    booking_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = Booking
        fields = ('class_type', 'booking_type', 'booking_date',
                  'time_slot',)
    