from django.contrib import admin
from hotels.models import Country, City, Amenity, Hotel

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Amenity)
admin.site.register(Hotel)
