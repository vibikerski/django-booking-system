# Generated by Django 5.0.2 on 2024-03-23 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0005_country_hotel_specific_location_alter_amenity_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='booking_system.city'),
            preserve_default=False,
        ),
    ]