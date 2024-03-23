from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from datetime import datetime
from booking_system.models import Booking
from rooms.models import Room


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
def get_bookings(request):
    user = request.user
    bookings = Booking.objects.filter(booked_by=user).order_by('start_date')
    context = {
        'bookings': bookings
    }
    
    return render(
        request,
        "booking_system/bookings.html",
        context
    )


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
        'success_booked': True,
    }

    return render(
        request,
        'rooms/room.html',
        context
    )


@login_required
def cancel_booking(request, booking_id):
    user = request.user
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.booked_by != user:
        raise PermissionDenied()
    
    booking.delete()
    
    bookings = Booking.objects.filter(booked_by=user).order_by('start_date')
    context = {
        'bookings': bookings
    }
    
    return render(
        request,
        "booking_system/bookings.html",
        context
    )
