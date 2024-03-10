from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from booking_system.models import Hotel, Room, Booking
from datetime import datetime, timedelta


def check_available(bookings, start, end):
    return not any(
        (start >= booking.start_date and start <= booking.end_date) or 
        (end >= booking.start_date and end <= booking.end_date)
        for booking in bookings
    )
    
    
def validate_date(bookings, start, end):
    try:
        start = datetime.strptime(start, '%Y-%m-%d').date()
        end = datetime.strptime(end, '%Y-%m-%d').date()
    except Exception:
        return False
    return False if start > end else check_available(bookings, start, end)


@login_required
def book_a_room(request, room_id):
    if request.method != "POST":
        return HttpResponse('Not allowed', 405)
    start_date = request.POST.get('start-date')
    end_date = request.POST.get('end-date')
    user = request.user

    room = get_object_or_404(Room, id=room_id)
    validated_date = validate_date(Booking.objects.filter(room=room), start_date, end_date)
    if not validated_date:
        return HttpResponse('Couldn\'t validate date', 400)

    booking = Booking(
        room=room, booked_by=user, start_date=start_date, end_date=end_date
    )
    booking.save()

    return HttpResponse(booking)


def get_booking_form(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    hotel_name = room.hotel.name
    hotel_id = room.hotel.id
        
    context = {
        'room': room,
        'hotel_name': hotel_name,
        'hotel_id': hotel_id,
        'authenticated': request.user.is_authenticated,
    }
    return render(
        request,
        'booking_system/booking_form.html',
        context
    )


def get_hotels(request):
    hotels = Hotel.objects.all()
    context = {
        'hotels': hotels
    }
    
    return render(
        request,
        'booking_system/hotels.html',
        context
    )


def get_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = Room.objects.filter(hotel=hotel)
    
    context = {
        'hotel': hotel,
        'rooms': rooms
    }
    
    return render(
        request,
        'booking_system/hotel.html',
        context
    )


def get_rooms_by_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = Room.objects.filter(hotel=hotel)
    rooms_list = list(rooms.values('id', 'name'))
    return JsonResponse(rooms_list, safe=False)


def get_taken_dates_for_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    bookings = Booking.objects.filter(room=room)

    taken_dates = []
    for booking in bookings:
        current_date = booking.start_date
        while current_date <= booking.end_date:
            taken_dates.append(current_date)
            current_date += timedelta(days=1)
    return JsonResponse({'dates': taken_dates})