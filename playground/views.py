from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hi(request):
    return HttpResponse('blablabla hihihi hohoho')


def say_hi_http_render(request):
    return render(request, "hello.html")
