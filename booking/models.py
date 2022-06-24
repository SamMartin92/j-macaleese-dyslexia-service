from django.db import models
from home.models import Client
# Create your models here.

BOOKING_TYPE = (
    ('Dyslexia Assesment', 'Dyslexia Assesment'),
    ('Intervention Class', 'Intervention Class'),
)

TIME_SLOTS = (
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
)

class Booking(models.Model):
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    booking_type = models.CharField(max_length=20, choices=BOOKING_TYPE, blank=False, null=False, help_text="What type of session would you like book?")
    booking_date = models.DateTimeField(blank=False, null=False)
    time_slot = models.CharField(max_length=20, blank=False, null=False, choices=TIME_SLOTS)
    