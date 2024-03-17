from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from booking_system.models import Hotel, Room, Booking, Review
from datetime import datetime, timedelta


# NOT USER-USED PAGES

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


# NON AUTHENTICATED DISPLAY

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
        'booking_system/room.html',
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
        'booking_system/hotel.html',
        context
    )


# AUTHENTICATED DISPLAY

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

# POST REQUESTS

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
        'booking_system/room.html',
        context
    )

@login_required
def review_a_room(request, room_id):
    if request.method != "POST":
        return HttpResponse('Not allowed', 405)
    user = request.user
    rating = request.POST.get('rating')
    feedback = request.POST.get('feedback')
    room = get_object_or_404(Room, id=room_id)
    
    review = Review(
        rating=rating,
        feedback=feedback,
        user=user,
        reviewed_object=room
    )
    review.save()
    
    return redirect("room", room_id)

@login_required
def review_a_hotel(request, hotel_id):
    user = request.user
    rating = request.POST.get('rating')
    feedback = request.POST.get('feedback')
    hotel = get_object_or_404(Hotel, id=hotel_id)
    
    review = Review(
        rating=rating,
        feedback=feedback,
        user=user,
        reviewed_object=hotel
    )
    review.save()
    
    return redirect("hotel", hotel_id)


@login_required
def cancel_booking(request, booking_id):
    user = request.user
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.booked_by != user:
        return HttpResponse(403)
    
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
