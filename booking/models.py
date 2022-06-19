from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    booking_id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.booking_id


class Client(models.Model):
    