from django.shortcuts import render, redirect
from .forms import *
from django.contrib.gis.geos import Point

def compte(request):
        if request.method == 'POST':
            formulaire = Form_User(request.POST)
            if formulaire.is_valid():
                formulaire.enregistrer()
                pseudo = formulaire.cleaned_data['pseudo']
                return redirect('map/')
            return render(request, 'app/signup.html', {'form': formulaire})
        return render(request, 'app/signup.html', {'form': Form_User()})

def add_node(request):
    # If a POST request is received, process the form data and save to the database
    if request.method == 'POST':
        mylatitude = request.POST.get('lat') 
        mylongitude = request.POST.get('lng') 
        point= Point(x=float(mylongitude),y=float(mylatitude))
        instance = nodes(Position=point, Latitude=mylatitude,Longitude=mylongitude)
        instance.save()
        return redirect('add_node')
    return render(request, 'app/maps.html', {})