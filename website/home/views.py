from django.shortcuts import render

# Create your views here.


def temp(request):
    return render(request,'app/base.html')
def home(request):
    return render(request,'app/home.html')