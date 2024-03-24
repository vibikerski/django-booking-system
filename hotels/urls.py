from django.urls import path
from hotels import views

urlpatterns = [
    path("hotels/", views.get_hotels, name="hotels"),
    path("hotels/<int:hotel_id>", views.get_hotel, name="hotel"),
    path("cities/<int:country_id>", views.get_cities, name="cities"),
    path("", views.main_page, name='main_page'),
]