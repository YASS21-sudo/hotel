from django.urls import path
from .views import RoomDetailsView, RoomsListView

urlpatterns = [
    path('', RoomsListView.as_view(), name='rooms_list'),
    path('room/<int:pk>', RoomDetailsView.as_view(), name='room_detail'),
]
