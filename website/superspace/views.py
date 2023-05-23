from django.shortcuts import render, redirect
from django.contrib.gis.geos import Point
from add_user.models import nodes,project,client,Post

def interface(request, psedo):
    projects= project.objects.all()
    nods = nodes.objects.all()
    nods1=""
    
    if request.method=="POST":
        button=request.POST.get("button")
        if button:
            project1= project.objects.get(id_projet=button)
            nods1 = nodes.objects.get(id_node=project1.nodeuser.id_node)
            data = Post.objects.filter(node=nods1).order_by('-id').first()
            print(data)
            return render(request, 'app/interface.html', {'nods': nods ,'projects':projects,"nods1":nods1,"project1":project1,"data":data})
        
            
    
    return render(request, 'app/interface.html', {'nods': nods ,'projects':projects,"nods1":nods1})

