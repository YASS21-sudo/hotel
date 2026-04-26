from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:room_id>/', views.book_room, name='book_room'),
    path('mes-reservations/', views.my_reservations, name='my_reservations'),
]
