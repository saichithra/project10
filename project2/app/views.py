from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('we are dreamer')
def second(request):
    return HttpResponse('<h1><marquee>i dont know anthing</h1></marquee>')
        