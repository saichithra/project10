from django.shortcuts import render

# Create your views here.
def stfile(request):
    return render(request,'stfiles.html')