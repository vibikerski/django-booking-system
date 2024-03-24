# Generated by Django 5.0.2 on 2024-03-23 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0006_hotel_city'),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='amenities',
        ),
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='room',
            name='facilities',
        ),
        migrations.RemoveField(
            model_name='room',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='review',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_type',
        ),
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rooms.room'),
        ),
        migrations.DeleteModel(
            name='Amenity',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Facility',
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='RoomType',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]