from django.urls import path
from . import views 

# URLConf
urlpatterns = [
    path('hi/', views.say_hi),
    path('hi2/', views.say_hi_http_render)
]