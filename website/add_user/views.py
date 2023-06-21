from django.shortcuts import render, redirect
from .forms import *
from django.contrib.gis.geos import Point
from .models import client,project
from .models import Post

def add_project(request, psedo):
  clients = client.objects.all()
  if request.method == 'POST':
    formul = form_project(request.POST)
    if formul.is_valid():
      formul.enregistrer()
      nom_de_projet = request.POST.get('nom_de_projet')
      region = request.POST.get('region')
      finp = request.POST.get('finp')
      debutp = request.POST.get('debutp')
      cl = request.POST.get('client')
      if cl == 'new_client':
        data = project(nom_de_projet=nom_de_projet, region=region, date_de_debut=debutp, date_de_fin=finp)
        data.save()
        return redirect('compte', data.id_projet, psedo)
      else:
        lient = client.objects.get(pk=cl)
        data = project(nom_de_projet=nom_de_projet, region=region, date_de_debut=debutp, date_de_fin=finp, clients=lient)
        data.save()
        return redirect('add_node', id_projet=data.id_projet, psedo=psedo)
    return render(request, 'app/add_project.html', {'formprojet':formul})
  return render(request, 'app/add_project.html', {'formprojet':form_project, 'clients':clients})

     


def compte(request, id_projet, psedo):
        project_instance = project.objects.get(id_projet=id_projet)

        if request.method == 'POST':
            formulaire = Form_User(request.POST)
            if formulaire.is_valid():
                formulaire.enregistrer(project_instance, psedo)
                return redirect('add_node',project_instance.id_projet, psedo)
            return render(request, 'app/signup.html', {'form': formulaire})
        return render(request, 'app/signup.html', {'form': Form_User()})

def add_node(request, id_projet, psedo):
    project_instance = project.objects.get(id_projet=id_projet)
    if request.method == 'POST':
        mylatitude = request.POST.get('lat')
        mylongitude = request.POST.get('lng')
        ref = request.POST.get('ref')
        print(ref)
        point = Point(x=float(mylongitude), y=float(mylatitude))

        node_instance = nodes(Position=point, Latitude=mylatitude, Longitude=mylongitude, ref=ref)
        node_instance.save()

        project_instance.nodeuser = node_instance
        project_instance.save()

        tem=0
        him=0
        instance = Post(temperature=tem,humidity=him)
        instance.save()

        instance.node=node_instance
        instance.save()
        
        print(psedo)
        
        return redirect('interface',psedo)
    return render(request, 'app/maps.html', {})