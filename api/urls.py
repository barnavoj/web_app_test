from django.urls import path
from . import views


urlpatterns = [
    path('room/create', views.RoomCreate.as_view()),
    path('room/show', views.RoomView.as_view()),
]
