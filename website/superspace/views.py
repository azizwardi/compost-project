from django.shortcuts import render, redirect
from django.contrib.gis.geos import Point
from add_user.models import nodes

def interface(request, psedo):
    nods = nodes.objects.all()
    return render(request, 'app/interface.html', {'nods': nods})

