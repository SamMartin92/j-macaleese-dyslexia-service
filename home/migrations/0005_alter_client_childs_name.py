# Generated by Django 4.0.5 on 2022-07-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_client_first_name_remove_client_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='childs_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]