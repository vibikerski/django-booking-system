from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from hotels.models import Hotel, City, Country
from rooms.models import Room


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


def main_page(request):
    countries = Country.objects.all().values('id', 'name')
    return render(
        request,
        'main_page.html',
        {'countries': countries}
    )
