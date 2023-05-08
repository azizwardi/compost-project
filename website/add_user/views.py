from django.shortcuts import render, redirect
from .forms import *
from django.contrib.gis.geos import Point
from .models import client

def add_project (request):
     clients=client.objects.all()
     if request.method =='POST':
          formul = form_project(request.POST)
          if formul.is_valid():
               formul.enregistrer()
               nom_de_projet = request.POST.get('nom_de_projet')
               region = request.POST.get('region')
               finp = request.POST.get('finp')
               debutp = request.POST.get('debutp')

               data = project(nom_de_projet=nom_de_projet, region=region,date_de_debut=debutp,date_de_fin=finp)
               data.save()
               bla =  request.POST.get('selecteditem')
               print(bla)
               if bla  == 'New Client':
                print(bla)
                return redirect('compte')
               else:
                return redirect('add_node')
               

          return render(request, 'app/add_project.html', {'formprojet':formul})
     return render(request, 'app/add_project.html', {'formprojet':form_project,'clients':clients}) 
     


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
