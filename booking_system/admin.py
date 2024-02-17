from django.contrib import admin
from booking_system.models import User, Hotel, Room, Booking

admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)