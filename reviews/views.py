from django.shortcuts import get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from reviews.models import Review
from rooms.models import Room
from hotels.models import Hotel


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
