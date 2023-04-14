from django.shortcuts import render

def tt(request):
    return render(request,'app/test.html')