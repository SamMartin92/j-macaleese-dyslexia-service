# Generated by Django 4.0.5 on 2022-08-15 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_alter_booking_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['status', 'booking_date', 'time_slot']},
        ),
        migrations.AddConstraint(
            model_name='booking',
            constraint=models.UniqueConstraint(fields=('booking_date', 'time_slot'), name='unique_time_slot'),
        ),
    ]
