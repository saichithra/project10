from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pasupathi(request):
    return render(request,'pasupathi.html')
