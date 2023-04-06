from django.shortcuts import render

# Create your views here.


def index(requset, *args, **kwargs):
    return render(requset, "frontend/index.html")
