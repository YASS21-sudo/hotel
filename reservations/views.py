from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rooms.models import Room
from .models import Reservation, ReservationItem

@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    reservation, created = Reservation.objects.get_or_create(user=request.user)
    
    item, item_created = ReservationItem.objects.get_or_create(reservation=reservation, room=room)
    if not item_created:
        item.quantity += 1
        item.save()
    
    messages.success(request, f"La chambre {room.name} a été ajoutée à vos réservations.")
    return redirect('my_reservations')

@login_required
def my_reservations(request):
    reservation = Reservation.objects.filter(user=request.user).first()
    return render(request, 'reservations/my_reservations.html', {'reservation': reservation})
