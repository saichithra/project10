from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insert_topic is submited')
    return render(request,'html_form.html')

def insert_webpage(request):
    if request.method=='POST':
        tn=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        T=Topic.Objects.get_or_create(topic_name=tn)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        W.save()
        return HttpResponse('insert_webpage is submited')
    return render(request,'webpage.html')