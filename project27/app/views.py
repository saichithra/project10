from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse

def insert_Topic(request):
    Tn=input('enter topic name')
    T=Topic.objects.get_or_create(Topic_name=Tn)[0]
    T.save()
    return HttpResponse('Topic is inserted successsefully')

def insert_Webpage(request):
    Tn=input('enter Topic_name')
    name=input('enter name')
    url=input('enter Url')
    T=Topic.objects.get_or_create(Topic_name=Tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(Topic_name=Tn,name=name,url=url)[0]
    W.save()
    return HttpResponse('Webpage  date inserted successsefully')

def insert_Access_Record(request):
    Tn=input('enter Topic_name')
    name=input('enter name')
    url=input('enter url')
    date=input('enter date')
    T=Topic.objects.get_or_create(Topic_name=Tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(Topic_name=Tn,name=name,url=url)[0]
    W.save()
    A=Access_Record.objects.get_or_create(name=W,date=date)
    A.save()
    return HttpResponse('Webpage  date inserted successsefully')