from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.gis.geos import Point
from add_user.models import nodes,project,client,Post
from add_user.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# @login_required(login_url='supervisor_login')
def interface(request, psedo):
    projects= project.objects.all()
    nods = nodes.objects.all()
    nods1=""
    
    if request.method=="POST":
        button=request.POST.get("button")
        delete_button=request.POST.get("delete_button")
        if button:
            project1= project.objects.get(id_projet=button)
            nods1 = nodes.objects.get(id_node=project1.nodeuser.id_node)
            data = Post.objects.filter(node=nods1).order_by('-id').first()
            
            return render(request, 'app/interface.html', {'nods': nods, 'projects': projects, "nods1": nods1, "project1": project1, "data": data, "psedo": psedo, "delete_project_id": project1.id_projet})
        
        elif delete_button:
            project_to_delete = project.objects.get(id_projet=delete_button)
            project_to_delete.delete()
            return redirect('interface', psedo=psedo)
        
            
    
    return render(request, 'app/interface.html', {'nods': nods ,'projects':projects,"nods1":nods1,"psedo":psedo})

# @login_required(login_url='supervisor_login')
def list(request, psedo):
    clientss = client.objects.all()
    return render(request, 'app/clientslist.html', {'clientss': clientss,'psedo' : psedo})


def delete_client(request,psedo,id):
    supervisor_obj = supervisor.objects.get(pseudo=psedo)
    clientt = client.objects.filter(supervisor=supervisor_obj)
    
    clientt = client.objects.get(id=id)
    
    clientt.delete()
    clientss = client.objects.all()
    return render(request, 'app/clientslist.html', {'clientss': clientss,'psedo' : psedo})
   


def modify_1(request, pseudo, id):

    supervisors = supervisor.objects.get(pseudo=pseudo)
    clientt = client.objects.filter(supervisor=supervisors)
    clientt = client.objects.get(id=id)

    
    if request.method == 'POST':

        formulairep = Form_User(request.POST)
        # Get the other data from the form data
        new_nom = request.POST.get('nom')
        new_prenom = request.POST.get('prenom')
        new_telephone = request.POST.get('NB_GSM')
        new_pseudo = request.POST.get('pseudo')
        new_email = request.POST.get('e_mail')


        if formulairep.is_valid():
            # Get the selected client from the form
            selected_client_id = request.POST.get('clientp')               
            formulairep.enregistrerProj()

            if selected_client_id:
                new_client = client.objects.get(id=selected_client_id)
                client.nom=new_nom
                client.prenom=new_prenom
                client.NB_GSM=new_telephone
                client.pseudo=new_pseudo
                client.e_mail=new_email
                client.clientp=new_client
                
                project.save()
                return redirect('ALL_node',pseudo=pseudo,id=project.polygon_id)
            else:
                project.nomp=new_name
                project.descp=new_descp
                project.debutp=new_debutp
                project.finp=new_finp
                project.cityp=new_cityp
                project.piece_joinde=new_piece_joinde
                project.save()              
                return redirect('ALL_node',pseudo=pseudo,id=project.polygon_id)

            
        return render(request, 'modify_1.html', {'form': formulairep,'projects':projects,'supervisor':supervisors})
    return render(request, 'modify_1.html', {'form': Form_project(),'projects':projects,'supervisor':supervisors})   

def modify_2(request, psedo, id):
        
        clienti = client.objects.get(id=id)
        project_instance = project.objects.filter(clients=clienti).order_by('-id_projet').first()
        


        if request.method == 'POST':
            formulaire = Form_User(request.POST)
            if formulaire.is_valid():
                formulaire.enregistrer1(project_instance, psedo, id)
                clientss = client.objects.all()
                return redirect(request, 'home')
            return render(request, 'app/signup.html', {'form': formulaire})
        return render(request, 'app/signup.html', {'form': Form_User()})