from django.db import models
from django.contrib.contenttypes import fields
from reviews.models import Review


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    name = models.CharField(max_length=127, unique=True)
    img = models.ImageField(upload_to='booking_system/sym', max_length=100, null=True, blank=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=511)
    description = models.TextField()
    image = models.ImageField(upload_to='booking_system/', max_length=100, null=True, blank=True)
    reviews = fields.GenericRelation(Review)
    amenities = models.ManyToManyField(Amenity, blank=True)
    
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    specific_location = models.CharField(max_length=511)
    
    def __str__(self):
        return self.name

    def location(self):
        return f'{self.city.country}, {self.city}, {self.specific_location}'
