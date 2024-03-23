from django.urls import path
from hotels import views

urlpatterns = [
    path("", views.get_hotels, name="hotels"),
    path("<int:hotel_id>", views.get_hotel, name="hotel"),
]