from django.db import models
import datetime
from django.db.models import  UniqueConstraint
from django.contrib.auth.models import User
# Create your models here.

CLASS_TYPE = (
    ('Dyslexia Assesment', 'Dyslexia Assesment'),
    ('Intervention Class', 'Intervention Class'),
)

BOOKING_TYPE = (
    ('Classroom', 'Classroom'),
    ('Virtual', 'Virtual'),
)

TIME_SLOTS = (
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
)

STATUS = ((0, "Pending"), (1, "Accepted"), (2, "Declined"), (3, "Completed"))


class Booking(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_type = models.CharField(max_length=20, choices=CLASS_TYPE, blank=False, null=False, default='', help_text="What type of session would you like book?")
    booking_type = models.CharField(max_length=20, choices=BOOKING_TYPE, blank=False, null=False)
    booking_date = models.DateField(blank=False, null=False, default=datetime.date.today)
    time_slot = models.CharField(max_length=20, blank=False, null=False, choices=TIME_SLOTS)
    status = models.IntegerField(choices=STATUS, default=0)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['status','booking_date', 'time_slot']
        UniqueConstraint(fields=['booking_date', 'time_slot'], name='unique_time_slot')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} : {self.booking_date}, {self.time_slot}"
    