from django.db import models
from guests.models import CustomUser
from rooms.models import Room

class Reservation(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='reservation')
    created_at = models.DateTimeField(auto_now_add=True)

class ReservationItem(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='items')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
