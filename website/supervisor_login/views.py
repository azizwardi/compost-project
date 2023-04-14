from django.shortcuts import render



def login1(request):
    return render(request,'app/supervisorlogin.html')