from django.shortcuts import render
from django.contrib.gis.geos import Point
from add_user.models import nodes
from add_user.models import client



def userinterface(request,pseudo):
    users=client.objects.get(pseudo=pseudo)
    mynode=users.nodeuser
    return render(request, 'app/user_interface.html',{'mynode':mynode})
