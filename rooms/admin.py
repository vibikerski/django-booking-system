from django.contrib import admin
from rooms.models import RoomType, Facility, Room

admin.site.register(RoomType)
admin.site.register(Facility)
admin.site.register(Room)
