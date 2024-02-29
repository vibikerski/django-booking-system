from booking_system import views
from django.urls import path

urlpatterns = [
    path("", views.get_hotels, name="hotels"),
    path("hotels/<int:hotel_id>", views.get_hotel, name="hotel"),
    path("rooms/<int:room_id>/booking", views.get_booking_form, name="booking_form"),
    path("rooms/by-hotel/<int:hotel_id>", views.get_rooms_by_hotel, name="rooms_by_hotel"),
    path("rooms/<int:room_id>/book", views.book_a_room, name="book"),
    path("rooms/<int:room_id>/taken", views.get_taken_dates_for_room, name="taken")
]