# Generated by Django 5.0.2 on 2024-03-01 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0003_rename_end_field_booking_end_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='available',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
