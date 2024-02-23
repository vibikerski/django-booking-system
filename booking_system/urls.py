from booking_system import views
from django.urls import path

urlpatterns = [
    path("", views.get_hotels, name="hotels"),
    path("hotels/<int:hotel_id>", views.get_hotel, name="hotel"),
    path("book", views.book_a_room, name="book"),
    path("booking", views.get_booking_form, name="booking_form"),
]