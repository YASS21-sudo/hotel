from django.shortcuts import render
from django.views import View
from .models import Room
from django.views.generic import ListView, DetailView

class RoomsListView(ListView):
    model = Room
    template_name = 'rooms/room_list.html'
    context_object_name = 'chambres'

class RoomDetailsView(DetailView):
    template_name = 'rooms/room_detail.html'
    model = Room
    context_object_name = 'room'
