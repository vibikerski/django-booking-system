from django.urls import path
from reviews import views


urlpatterns = [
    path("hotels/<int:hotel_id>/review", views.review_a_hotel, name="review_hotel"),
    path("rooms/<int:room_id>/review", views.review_a_room, name="review_room"),
]