from django.db import models
from django.conf import settings

class Image(models.Model):
    url = models.CharField(max_length=255)
    alt_text = models.CharField(max_length=1023, blank=True, null=True)
    
    def __str__(self):
        return self.alt_text

class Hotel(models.Model):
    name = models.CharField(max_length=511)
    description = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length = 127)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
    
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    booked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.room.name