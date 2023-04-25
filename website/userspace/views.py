from django.shortcuts import render

# Create your views here.

def userinterface(request):
     return render(request,'app/user_interface.html')