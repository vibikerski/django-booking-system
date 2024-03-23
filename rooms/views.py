from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from datetime import timedelta
from hotels.models import Hotel
from rooms.models import Room
from booking_system.models import Booking


def get_rooms_by_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = Room.objects.filter(hotel=hotel)
    rooms_list = list(rooms.values('id', 'name'))
    return JsonResponse(rooms_list, safe=False)


def get_taken_dates_for_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    bookings = Booking.objects.filter(room=room)

    taken_dates = [
        current_date
        for booking in bookings
        for current_date in (
            booking.start_date + timedelta(days=n)
            for n in range((booking.end_date - booking.start_date).days + 1)
        )
    ]
    return JsonResponse({'dates': taken_dates})


def get_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    hotel_name = room.hotel.name
    hotel_id = room.hotel.id
    reviews = room.reviews.all()
    review_url = reverse('review_room', args=[room_id])
        
    context = {
        'room': room,
        'hotel_name': hotel_name,
        'hotel_id': hotel_id,
        'authenticated': request.user.is_authenticated,
        'reviews': reviews,
        'review_url': review_url,
    }
    return render(
        request,
        'rooms/room.html',
        context
    )
