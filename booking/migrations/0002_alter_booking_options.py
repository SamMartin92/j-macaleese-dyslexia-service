# Generated by Django 4.0.5 on 2022-06-30 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['booking_date', 'time_slot']},
        ),
    ]