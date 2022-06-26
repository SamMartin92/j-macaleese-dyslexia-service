from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=50, null=False, blank=False)
    # last_name = models.CharField(max_length=50, null=False, blank=False, default='')
    phone = PhoneNumberField(null=False, blank=False)
    is_guardian = models.BooleanField(default=False, null=False, blank=False)
    childs_name = models.CharField(max_length=50)
    already_diagnosed = models.BooleanField(default=False, null=False, blank=False)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @receiver(post_save, sender=User)
    def create_client(sender, instance, created, **kwargs):
        if created:
            Client.objects.create(user=instance)
        

    @receiver(post_save, sender=User)
    def save_client(sender, instance, **kwargs):
        instance.client.save()
    





