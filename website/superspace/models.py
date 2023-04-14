from django.db import models
from django.contrib.gis.db import models 
from django.contrib.gis.admin import OSMGeoAdmin

class user(models.Model):
    nom=models.CharField(max_length=100,null=True)
    prenom=models.CharField(max_length=100,null=True)
    NB_GSM=models.CharField(max_length=100,null=True)
    pseudo=models.CharField(max_length=100,null=True)
    e_mail=models.EmailField(max_length=100,null=True)
    position=models.PointField(null=True)
    image=models.ImageField(null=True)
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    


class nodes(models.Model):
    Name = models.CharField(max_length=50,blank=True, null=True)
    Position=models.PointField(null=True)
    Latitude =models.CharField(max_length=50, null=True , blank=True)
    Longitude =models.CharField(max_length=50, null=True,blank=True)
    
    def __str__(self):
        return "Node " + str(self.id) 
    
    class Meta:
       verbose_name_plural = "Nodes"
       verbose_name = "Node"


class nodesAdmin(OSMGeoAdmin):
    list_display = ('Name', 'Latitude', 'Longitude')
    search_fields = ('Name',)
    list_filter = ('Name',)


