from django.shortcuts import redirect, render
from django.contrib.gis.geos import Point
from add_user.models import nodes
from add_user.models import client,project,Post
from django.http import JsonResponse


def projectlist(request,pseudo):
    users= client.objects.get(pseudo=pseudo)
    projects = project.objects.filter(clients=users)
    if request.method=="POST":
        button=request.POST.get("button")
        if button:
           idbutton=button
           return redirect('user_interface', pseudo=pseudo, idbutton=idbutton)

    return render(request,'app/projectlist.html', {'pseudo':pseudo,'projects':projects} )


def userinterface(request, pseudo ,idbutton):
    project1 = project.objects.get(id_projet=idbutton)
    nods = nodes.objects.get(id_node=project1.nodeuser.id_node)
    data = Post.objects.filter(node=nods).order_by('-id').first()
    tem = data.temperature
    hum = data.humidity
    dattta = []
    dattta.append({
        'temperature': tem,
        'humidity': hum,
     })
    ltemp =[]
    dss = Post.objects.filter(node=nods).order_by('-id')
    for d in dss : 
        ltemp.append(
            d.temperature,
        )
    lhum =[]
    dss = Post.objects.filter(node=nods).order_by('-id')
    for d in dss :   
        lhum.append(
            d.humidity,
        )
    context = {
            'temperature': tem,
            'humidity': hum,
            'pseudo': pseudo,
            'nods' : nods,
            'data' : data,
            'idbutton' : idbutton,
            'ltemp':ltemp,
            'lhum':lhum,
             }   
    
    return render(request, 'app/user_interface.html', context)

def mq(idbutton):
    print("la3ziz")
    project1 = project.objects.get(id_projet=idbutton)
    nods = nodes.objects.get(id_node=project1.nodeuser.id_node)
    data = Post.objects.filter(nods=nods).order_by('-id').first()
    tem = data.temperature
    hum = data.humidity
    date = data.published_date
    dattta = []
    dattta.append({
        'temperature': tem,
        'humidity': hum,
        'published_date' : date,
     })
    print(dattta)
    return JsonResponse(dattta, safe=False)