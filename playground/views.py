from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hi(request):
    return HttpResponse('blablabla hihihi hohoho')