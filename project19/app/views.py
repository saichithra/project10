from django.shortcuts import render

# Create your views here.
def cd(request):
    return render(request,'cd.html')