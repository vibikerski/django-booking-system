from booking_system import views
from django.urls import path

urlpatterns = [
    path("", views.get_hotels, name="hotels"),
    path("hotels/<int:hotel_id>", views.get_hotel, name="hotel"),
    path("hotels/<int:hotel_id>/review", views.review_a_hotel, name="review_hotel"),
    path("rooms/<int:room_id>", views.get_room, name="room"),
    path("rooms/<int:room_id>/book", views.book_a_room, name="book"),
    path("rooms/<int:room_id>/taken", views.get_taken_dates_for_room, name="taken"),
    path("rooms/<int:room_id>/review", views.review_a_room, name="review_room"),
    path("rooms/by-hotel/<int:hotel_id>", views.get_rooms_by_hotel, name="rooms_by_hotel"),
    path("account/bookings", views.get_bookings, name="bookings"),
]