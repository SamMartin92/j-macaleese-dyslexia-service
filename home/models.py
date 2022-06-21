from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = PhoneNumberField(null=False)
    ## email should be here
    is_guardian = models.BooleanField(default=False)
    childs_name = models.CharField(max_length=50, null=True)
    already_diagnosed = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    




class Booking(models.Model):
    booking_id = models.IntegerField()
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)


    def __str__(self):
        return self.booking_id

