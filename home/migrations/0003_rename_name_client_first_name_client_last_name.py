# Generated by Django 4.0.5 on 2022-06-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_delete_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
