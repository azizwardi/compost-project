from django.shortcuts import render, redirect
from .forms import *
from django.contrib.gis.geos import Point
from django.core.serializers import serialize


# Create your views here.

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

    # Retrieve all existing node positions from the database
    # all_nodes = nodes.objects.all()
    # node_positions = []
    # for node in all_nodes:
    #     node_positions.append([node.Latitude, node.Longitude])

    # # Render the template with existing node positions
    # return render(request, 'app/maps.html', {'node_positions': node_positions})
 


def interface(request):
    nods = nodes.objects.all()
    return render(request, 'app/interface.html', {'nods': nods})

