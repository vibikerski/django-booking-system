from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from hotels.models import Hotel, City, Country
from rooms.models import Room, RoomType


def get_cities(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    cities = City.objects.filter(country=country).values('id', 'name')
    return JsonResponse(list(cities), safe=False)


def get_hotels(request):
    if city_id := request.GET.get('city'):
        city = get_object_or_404(City, id=city_id)
        hotels = Hotel.objects.filter(city=city)
    elif country_id := request.GET.get('country'):
        country = get_object_or_404(Country, id=country_id)
        hotels = Hotel.objects.filter(city__country=country)
    else:
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
    
    room_types = RoomType.objects.all()
    
    if capacity := request.GET.get("capacity"):
        rooms = rooms.filter(capacity=capacity)
    if min_price := request.GET.get("min_price"):
        rooms = rooms.filter(current_price__gte=min_price)
    if max_price := request.GET.get("max_price"):
        rooms = rooms.filter(current_price__lte=max_price)
    if room_type_id := request.GET.get("room_type"):
        room_type = get_object_or_404(RoomType, id=room_type_id)
        rooms = rooms.filter(room_type=room_type)

    reviews = hotel.reviews.all()
    review_url = reverse('review_hotel', args=[hotel_id])
    
    context = {
        'hotel': hotel,
        'rooms': rooms,
        'authenticated': request.user.is_authenticated,
        'reviews': reviews,
        'review_url': review_url,
        'room_types': room_types,
    }
    
    return render(
        request,
        'hotels/hotel.html',
        context
    )


def main_page(request):
    countries = Country.objects.all().values('id', 'name')
    return render(
        request,
        'main_page.html',
        {'countries': countries}
    )
