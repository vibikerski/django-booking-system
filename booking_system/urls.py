from booking_system import views
from django.urls import path

urlpatterns = [
    path("rooms/<int:room_id>/book", views.book_a_room, name="book"),
    path("account/bookings", views.get_bookings, name="bookings"),
    path("account/bookings/<int:booking_id>/cancel", views.cancel_booking, name="remove_booking"),
]