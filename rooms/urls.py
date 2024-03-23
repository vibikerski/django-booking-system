from rooms import views
from django.urls import path

urlpatterns = [
    path("<int:room_id>", views.get_room, name="room"),
    path("<int:room_id>/taken", views.get_taken_dates_for_room, name="taken"),
    path("by-hotel/<int:hotel_id>", views.get_rooms_by_hotel, name="rooms_by_hotel"),
]