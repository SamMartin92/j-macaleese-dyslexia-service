from django.db import models
import datetime
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
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='client_id')
    booking_type = models.CharField(max_length=20, choices=BOOKING_TYPE, blank=False, null=False, help_text="What type of session would you like book?")
    booking_date = models.DateField(blank=False, null=False, default=datetime.date.today)
    time_slot = models.CharField(max_length=20, blank=False, null=False, choices=TIME_SLOTS)

    def __str__(self):
        return f"{self.Client.name} : {self.booking_date}, {self.time_slot}"
    