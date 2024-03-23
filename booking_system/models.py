from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields

class Review(models.Model):
    rating = models.IntegerField(
        validators = [
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    feedback = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    reviewed_object = fields.GenericForeignKey('content_type', 'object_id')


class Amenity(models.Model):
    name = models.CharField(max_length=127, unique=True)
    img = models.ImageField(upload_to='booking_system/sym', max_length=100, null=True, blank=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=511)
    description = models.TextField()
    image = models.ImageField(upload_to='booking_system/', max_length=100, null=True, blank=True)
    reviews = fields.GenericRelation(Review)
    amenities = models.ManyToManyField(Amenity)
    
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    specific_location = models.CharField(max_length=511)
    
    def __str__(self):
        return self.name

    def location(self):
        return f'{self.city.country}, {self.city}, {self.specific_location}'


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
    facilities = models.ManyToManyField(Facility)
    current_price = models.IntegerField(validators=[MinValueValidator(1)])
    
    def __str__(self):
        return self.name
    
    
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    booked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.room.name
