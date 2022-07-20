from django import forms
from django.forms.widgets import NumberInput
from .models import Booking, CLASS_TYPE, BOOKING_TYPE, TIME_SLOTS, STATUS

# CLASS_TYPE = (
#     ('Dyslexia Assesment', 'Dyslexia Assesment'),
#     ('Intervention Class', 'Intervention Class'),
# )

# BOOKING_TYPE = (
#     ('Classroom', 'Classroom'),
#     ('Virtual', 'Virtual'),
# )

# TIME_SLOTS = (
#     ('17:00', '17:00'),
#     ('18:00', '18:00'),
#     ('19:00', '19:00'),
#     ('20:00', '20:00'),
# )

# STATUS = ((0, "Pending"), (1, "Accepted"), (2, "Declined"), (3, "Completed"))

class BookingForm(forms.ModelForm):

    class_type = forms.ChoiceField(choices=CLASS_TYPE, label="Class type")
    booking_type = forms.ChoiceField(choices=BOOKING_TYPE, label="Classroom or Virtual")
    booking_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label = "Date ")
    time_slot = forms.ChoiceField(choices=TIME_SLOTS, label="Time")
    class Meta:
        model = Booking
        fields = ('class_type', 'booking_type', 'booking_date',
                  'time_slot',)
    