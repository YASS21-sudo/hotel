from django.contrib import admin
from .models import Reservation, ReservationItem

class ReservationItemInline(admin.TabularInline):
    model = ReservationItem
    extra = 0

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']
    inlines = [ReservationItemInline]

