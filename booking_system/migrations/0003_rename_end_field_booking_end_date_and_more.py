# Generated by Django 5.0.2 on 2024-02-17 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0002_alter_booking_end_field_alter_booking_start_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='end_field',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='start_time',
            new_name='start_date',
        ),
    ]
