from django.shortcuts import render
from django.contrib.gis.geos import Point
from add_user.models import nodes
from add_user.models import client,project



def userinterface(request,pseudo):
    users=client.objects.get(pseudo=pseudo)
    projects = project.objects.filter(clients=users)
    nods = nodes.objects.all()
    mynode=""
    if request.method=="POST":
        button=request.POST.get("button")
        if button:
            project1= project.objects.get(id_projet=button)
            mynode = nodes.objects.get(id_node=project1.nodeuser.id_node)
            return render(request, 'app/user_interface.html', {'nods': nods ,'projects':projects,"mynode":mynode})
        
    return render(request, 'app/user_interface.html',{'nods': nods ,'projects':projects,"mynode":mynode})
