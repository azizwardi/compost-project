from django.db import models
from django.contrib.gis.db import models 

class supervisor(models.Model):
    nom=models.CharField(max_length=100,null=True)
    prenom=models.CharField(max_length=100,null=True)
    NB_GSM=models.CharField(max_length=100,null=True)
    pseudo=models.CharField(max_length=100,null=True)
    e_mail=models.EmailField(max_length=100,null=True)
    password = models.CharField(max_length=128, null=True)
    image=models.ImageField(null=True)
    def __str__(self):
        return f"{self.prenom} {self.nom}"


