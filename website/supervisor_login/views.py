from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *

def login1(request):
    if request.method == 'POST':
        # If the request method is POST, process the form data
        formulaire = LoginForm(request.POST)
        if formulaire.is_valid(request):
            # If the form is valid, attempt to authenticate the user
            pseudo = formulaire.cleaned_data['pseudo']
            mot_de_passe = formulaire.cleaned_data['mot_de_passe']
            data = authenticate(request, username=pseudo, password=mot_de_passe)
            if data is not None:
                # If authentication is successful, log in the user and redirect to home page
                login(request, data)
                return redirect('interface')
        # If the form is not valid or authentication fails, re-render the form with any error messages
        return render(request, 'app/supervisorlogin.html', {'form': formulaire})
    else:
        # If the request method is not POST, render the login form
        return render(request, 'app/supervisorlogin.html', {'form': LoginForm()})




# def login1(request):
#     return render(request,'app/supervisorlogin.html')