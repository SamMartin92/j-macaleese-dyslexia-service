from django import forms
from django.forms.widgets import NumberInput
from .models import Booking, CLASS_TYPE, BOOKING_TYPE, TIME_SLOTS


class BookingForm(forms.ModelForm):

    class_type = forms.ChoiceField(choices=CLASS_TYPE, label="Class type")
    booking_type = forms.ChoiceField(
        choices=BOOKING_TYPE,
        label="Classroom or Virtual")
    booking_date = forms.DateField(
        widget=NumberInput(
            attrs={
                'type': 'date'}),
        label="Date ")
    time_slot = forms.ChoiceField(choices=TIME_SLOTS, label="Time")

    class Meta:
        model = Booking
        fields = ('class_type', 'booking_type', 'booking_date',
                  'time_slot',)
