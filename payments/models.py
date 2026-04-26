from django.db import models
from guests.models import CustomUser
from rooms.models import Room

class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='payments')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='En attente')
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField()

class PaymentItem(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='items')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
