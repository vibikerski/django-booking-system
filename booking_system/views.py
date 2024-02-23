from django.shortcuts import render, get_object_or_404, HttpResponse
from booking_system.models import User, Hotel, Room, Booking
from datetime import datetime

def check_available(bookings, start, end):
    start = datetime(*start.split('-'))
    end = datetime(*end.split('-'))
    return not any(
        start < booking.end_date or end > booking.start_date
        for booking in bookings
    )

def book_a_room(request):
    if request.method != "POST":
        return HttpResponse('Not allowed', 405)
    room_id = request.POST.get('room-id')
    start_date = request.POST.get('start-date')
    end_date = request.POST.get('end-date')

    email = request.POST.get('email')
    try:
        user = User.objects.get(email=email)
    except Exception:
        username = request.POST.get('user-name')
        user = User(
            full_name=username,
            email=email
        )

    room = get_object_or_404(Room, id=room_id)
    if not check_available(Booking.objects.filter(room=room), start_date, end_date):
        return HttpResponse('Not available', 400)

    return Booking(
        room=room, booked_by=user, start_date=start_date, end_date=end_date
    )

def get_booking_form(request):
    pass # TODO: RENDER WITH TEMPLATES
    # TODO: ONLY ALLOW SELECTING AVAILABLE DATES IN TEMPLATE (to justify httpresponse bad request)

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
