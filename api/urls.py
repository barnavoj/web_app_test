from django.urls import path
from . import views


urlpatterns = [
    path('room/create', views.CreateRoomView.as_view()),
    path('room/show', views.RoomView.as_view()),
    path('get-room', views.GetRoom.as_view())
]
