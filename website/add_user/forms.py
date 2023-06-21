from django import forms
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from .models import *
from supervisor_login.models import *
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class form_project(forms.Form):
    nom_de_projet = forms.CharField(required=True, max_length=project._meta.get_field(
        'nom_de_projet').max_length, widget=forms.TextInput(attrs={'id': "nom_de_projet", 'name': "nom_de_projet", 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px", 'placeholder': 'nom de projet'}))
    region = forms.CharField(required=True, max_length=project._meta.get_field(
        'region').max_length, widget=forms.TextInput(attrs={'id': 'region', 'name': 'region', 'placeholder': 'region', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
  
    def is_valid(self):
        nom_de_projet = self.data['nom_de_projet']
        if project.objects.filter(nom_de_projet=nom_de_projet).exists():
            self.add_error("nom_de_projet", "nom déja existant!")
        region = self.data['region']
        if any(char.isdigit() for char in region):
            self.add_error("region", "region est incorrect!")            

        value = super(form_project, self).is_valid()
        return value
    
    def enregistrer(self):
        nom_de_projet = self.cleaned_data['nom_de_projet']
        # pays = self.cleaned_data['region']
        




class Form_User(forms.Form):
    nom = forms.CharField(required=True, max_length=client._meta.get_field(
        'nom').max_length, widget=forms.TextInput(attrs={'id': "nom", 'name': "nom", 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px", 'placeholder': 'Nom'}))
    prenom = forms.CharField(required=True, max_length=client._meta.get_field(
        'prenom').max_length, widget=forms.TextInput(attrs={'id': 'prenom', 'name': 'prenom', 'placeholder': 'Prénom', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    telephone = forms.CharField(required=True, max_length=client._meta.get_field(
        'NB_GSM').max_length, widget=forms.TextInput(attrs={'id': 'NB_GSM', 'name': 'NB_GSM', 'placeholder': 'Téléphone', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    pseudo = forms.CharField(required=True, max_length=client._meta.get_field(
        'pseudo').max_length, widget=forms.TextInput(attrs={'id': 'pseudo', 'name': 'pseudo', 'placeholder': 'Pseudo', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    email = forms.EmailField(max_length=client._meta.get_field(
        'e_mail').max_length, required=True, widget=forms.EmailInput(attrs={'id': 'email', 'name': 'email', 'placeholder': 'E-Mail', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'id': 'password', 'name': 'password', 'placeholder': 'Mot de passe', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    confirmation_mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'id': 'password1', 'name': 'password1', 'placeholder': 'Re-saisir le mot de passe', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    
    def is_valid(self):
        nom = self.data['nom']
        if any(char.isdigit() for char in nom):
            self.add_error("nom", "Nom est incorrect!")
        prenom = self.data['prenom']
        if any(char.isdigit() for char in prenom):
            self.add_error("prenom", "Prenom est incorrect!")
        pseudo = self.data['pseudo']
        if client.objects.filter(pseudo=pseudo).exists():
            self.add_error("pseudo", "pseudo déja existant!")
        email = self.data['email']
        if client.objects.filter(e_mail=email).exists():
            self.add_error("email", "email déja existant!")
        telephone = self.data['telephone']
        if not telephone.isdigit():
            self.add_error("telephone", "Téléphone est incorrect!")
        mot_de_passe = self.data['mot_de_passe']
        if len(mot_de_passe) < 8:
            self.add_error(
                "mot_de_passe", "Le mot de passe doit contenir au moins 8 caractères.")
        confirmation_mot_de_passe = self.data['confirmation_mot_de_passe']
        if confirmation_mot_de_passe != mot_de_passe:
            self.add_error("confirmation_mot_de_passe",
                           "Les mots de passe ne correspondent pas.")
        value = super(Form_User, self).is_valid()
        return value

    def enregistrer(self,project_instance, psedo):
        nom = self.cleaned_data['nom']
        prenom = self.cleaned_data['prenom']
        email = self.cleaned_data['email']
        pseudo = self.cleaned_data['pseudo']
        telephone = self.cleaned_data['telephone']
        confirmation_mot_de_passe = self.cleaned_data['confirmation_mot_de_passe']
        sv= supervisor.objects.get(pseudo=psedo)
        data = client(nom=nom, prenom=prenom, pseudo=pseudo,
                          NB_GSM=telephone, e_mail=email)
        data.save()


        data.supervisor=sv
        data.save()
                
        project_instance.clients=data
        project_instance.save()
        data= User.objects.create_user(
            pseudo, email, confirmation_mot_de_passe)
        data.save()
            # Get the client email entered by the user
            # client_email = request.POST.get('client_email')
            
            # Prepare the email subject and message
        subject = 'Client data!'
        context = { 
                'nom': nom,
                'prenom': prenom,
                'email': email,
                'phone': telephone,
                'mdp': confirmation_mot_de_passe, 
                'pseudo' : pseudo,
            }
        html_message = render_to_string('app/email_template.html', context)
        plain_message = strip_tags(html_message)
            
            # Send the email
        send_mail(subject, plain_message, 'wardiaziz2507@gmail.com', [email], html_message=html_message)     




    def enregistrer1(self,project_instance, psedo, id):
        nom = self.cleaned_data['nom']
        prenom = self.cleaned_data['prenom']
        email = self.cleaned_data['email']
        pseudo = self.cleaned_data['pseudo']
        telephone = self.cleaned_data['telephone']
        confirmation_mot_de_passe = self.cleaned_data['confirmation_mot_de_passe']
        sv= supervisor.objects.get(pseudo=psedo)

        dataa = client.objects.get(id=id)
        # data = client(nom=nom, prenom=prenom, pseudo=pseudo,
        #                  NB_GSM=telephone, e_mail=email)
        # data.save()
        dataa.nom=nom
        dataa.save()

        dataa.prenom=prenom
        dataa.save()

        dataa.pseudo=pseudo
        dataa.save()

        dataa.NB_GSM=telephone
        dataa.save()

        dataa.e_mail=email
        dataa.save()
        
        dataa.supervisor=sv
        dataa.save()
                
     

            # Get the client email entered by the user
            # client_email = request.POST.get('client_email')
            
            # Prepare the email subject and message
        subject = 'Client data!'
        context = { 
                'nom': nom,
                'prenom': prenom,
                'email': email,
                'phone': telephone,
                'mdp': confirmation_mot_de_passe, 
                'pseudo' : pseudo,
            }
        html_message = render_to_string('app/email_template.html', context)
        plain_message = strip_tags(html_message)
            
            # Send the email
        send_mail(subject, plain_message, 'wardiaziz2507@gmail.com', [email], html_message=html_message)     


class position(forms.Form):
    latitude = forms.FloatField(required=False, widget=forms.HiddenInput(
        attrs={'id': 'lat', 'name': 'lat'}))
    longitude = forms.FloatField(required=False, widget=forms.HiddenInput(
        attrs={'id': 'lng', 'name': 'lng'}))

    def is_valid(self):
        lat = self.data['latitude']
        lng = self.data['longitude']
        if lat == '' or lng == '':
            self.add_error("latitude", "choisit votre position")
        value = super(position, self).is_valid()
        return value

    def enregistrer_client(self, pseudo):
        lat = self.cleaned_data['latitude']
        lng = self.cleaned_data['longitude']
        point = Point(x=float(lng), y=float(lat))
        data = client.objects.get(pseudo=pseudo)
        if data:
            data.position = point
            data.save()
