from django.urls import path
from . import views


urlpatterns = [
    path('room/modify', views.CreateRoomView.as_view()),
    path('room/create', views.RoomCreate.as_view()),
    path('room/show', views.RoomView.as_view()),
]
