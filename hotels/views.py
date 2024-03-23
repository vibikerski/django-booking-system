from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from hotels.models import Hotel
from rooms.models import Room


def get_hotels(request):
    hotels = Hotel.objects.all()
    context = {
        'hotels': hotels
    }
    
    return render(
        request,
        'hotels/hotels.html',
        context
    )


def get_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = Room.objects.filter(hotel=hotel)
    reviews = hotel.reviews.all()
    review_url = reverse('review_hotel', args=[hotel_id])
    
    context = {
        'hotel': hotel,
        'rooms': rooms,
        'authenticated': request.user.is_authenticated,
        'reviews': reviews,
        'review_url': review_url,
    }
    
    return render(
        request,
        'hotels/hotel.html',
        context
    )
