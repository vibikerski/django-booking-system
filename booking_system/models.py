from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.full_name

class Hotel(models.Model):
    name = models.CharField(max_length=511)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length = 127)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.room.name