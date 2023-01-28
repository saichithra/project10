from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from app.models import *
def display_topic(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='CRICKET')
    QST=Topic.objects.all()
    d={'Topic':QST}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='CRICKET')
    QSW=Webpage.objects.exclude(topic_name='CRICKET')
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.all().order_by('-name')
    QSW=Webpage.objects.filter(topic_name='KABADDI').order_by('-name')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(url__startswith='https')
    QSW=Webpage.objects.filter(url__startswith='http')
    QSW=Webpage.objects.filter(name__startswith='R')
    QSW=Webpage.objects.filter(name__contains='L')
    QSW=Webpage.objects.filter(name__regex='\w{6}')
    QSW=Webpage.objects.filter(name__in=['MSD','LUCKEY','RAM'])
    QSW=Webpage.objects.filter(Q(topic_name='CRICKET') | Q(name='MSD'))
    QSW=Webpage.objects.filter(Q(topic_name='CRICKET') | Q(url__startswith='https'))
    d={'webpage':QSW}
    return render(request,'display_webpage.html',d)


def display_accessrecord(request):
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date='2002-1-11')
    QSA=AccessRecords.objects.filter(date__gt='2002-1-11')
    QSA=AccessRecords.objects.filter(date__gte='2002-1-11')
    QSA=AccessRecords.objects.filter(date__lte='2002-1-11')
    QSA=AccessRecords.objects.filter(date__year='2004')
    QSA=AccessRecords.objects.filter(date__month='5')
    QSA=AccessRecords.objects.filter(date__day='11')
    QSA=AccessRecords.objects.filter(date__year__gte='2001')
    d={'AccessRecords':QSA}
    return render(request,'display_accessrecord.html',d)

def update_webpage(request):
   # Webpage.objects.filter(name='MSD').update(url='http://msd.com')
    Webpage.objects.filter(topic_name='KABADDI').update(name='LUCKEY')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.all()
    d={'webpage':QSW}
    return render(request,'display_webpage.html',d)
    