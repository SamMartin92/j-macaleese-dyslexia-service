# Generated by Django 4.0.5 on 2022-07-18 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_booking_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['status', 'booking_date', 'time_slot']},
        ),
    ]