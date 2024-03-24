from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.contenttypes import fields
from reviews.models import Review
from hotels.models import Hotel


class RoomType(models.Model):
    name = models.CharField(max_length=127)
    capacity = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(max_length=127, unique=True)
    img = models.ImageField(upload_to='booking_system/sym', max_length=100, null=True, blank=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=127)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='booking_system/', max_length=100, null=True, blank=True)
    reviews = fields.GenericRelation(Review)
    facilities = models.ManyToManyField(Facility, blank=True)
    current_price = models.IntegerField(validators=[MinValueValidator(1)])
    
    def __str__(self):
        return self.name
