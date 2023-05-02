from django.shortcuts import render, redirect
from .forms import *
from django.contrib.gis.geos import Point

def compte(request):
        if request.method == 'POST':
            formulaire = Form_User(request.POST)
            if formulaire.is_valid():
                formulaire.enregistrer()
                pseudo = formulaire.cleaned_data['pseudo']
                return redirect('add_node',pseudo)
            return render(request, 'app/signup.html', {'form': formulaire})
        return render(request, 'app/signup.html', {'form': Form_User()})

def add_node(request, pseudo):
    user_instance = client.objects.get(pseudo=pseudo)
    if request.method == 'POST':
        mylatitude = request.POST.get('lat')
        mylongitude = request.POST.get('lng')
        point = Point(x=float(mylongitude), y=float(mylatitude))

        node_instance = nodes(Position=point, Latitude=mylatitude, Longitude=mylongitude)
        node_instance.save()

        user_instance.nodeuser = node_instance
        user_instance.save()

        return redirect('interface')
    return render(request, 'app/maps.html', {})
