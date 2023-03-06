from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def asif(request):
    return HttpResponse("<h1>he is my friend</h1>")

def narendra(request):
    return HttpResponse('<h2>he is also my friend</h2>')

def choti(request):
    return HttpResponse("<marquee><h1>she is my bestie</h1></marquee>")