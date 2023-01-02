from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'sai','l':[11,22,33]}
    return render(request,'looping.html',d)