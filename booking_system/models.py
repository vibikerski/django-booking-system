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

class Hotel(models.Model):
    name = models.CharField(max_length=511)
    description = models.TextField()
    image = models.ImageField(upload_to='booking_system/', max_length=100, null=True, blank=True)
    reviews = fields.GenericRelation(Review)
    
    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length = 127)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='booking_system/', max_length=100, null=True, blank=True)
    reviews = fields.GenericRelation(Review)
    
    def __str__(self):
        return self.name
    
    
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    booked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.room.name