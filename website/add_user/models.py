from django.db import models
from django.contrib.gis.db import models 
from django.contrib.gis.admin import OSMGeoAdmin
from django.utils import timezone



class project(models.Model):
    id_projet= models.AutoField(primary_key=True, default=None)
    nom_de_projet=models.CharField(max_length=200,null=True)
    region=models.CharField(max_length=100,null=True)
    date_de_debut=models.DateTimeField(max_length=100,null=True)
    date_de_fin=models.DateTimeField(max_length=100,null=True)

    clients=models.ForeignKey('add_user.client', on_delete=models.CASCADE, null=True, related_name='client')
    nodeuser=models.ForeignKey('add_user.nodes', on_delete=models.CASCADE, null=True, related_name='node')
    def __str__(self):
        return f"{self.nom_de_projet}"






class client(models.Model):
    
    nom=models.CharField(max_length=100,null=True)
    prenom=models.CharField(max_length=100,null=True)
    NB_GSM=models.CharField(max_length=100,null=True)
    pseudo=models.CharField(max_length=100,null=True)
    e_mail=models.EmailField(max_length=100,null=True)
    position=models.PointField(null=True)
    image=models.ImageField(null=True)


    supervisor=models.ForeignKey('supervisor_login.supervisor', on_delete=models.CASCADE, null=True, related_name='supervisor')
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    


class nodes(models.Model):
    id_node= models.AutoField(primary_key=True, default=None)
    Name = models.CharField(max_length=50,blank=True, null=True)
    Description = models.CharField(max_length=100,blank=True, null=True)
    Position=models.PointField(null=True)
    Latitude =models.CharField(max_length=50, null=True , blank=True)
    Longitude =models.CharField(max_length=50, null=True,blank=True)
    RSSI = models.BigIntegerField(null=True)
    ref =  models.CharField(max_length=50, null=True)
    snr =  models.CharField(max_length=50, null=True)


    def __str__(self):
        return "Node " + str(self.id_node) 
    
    class Meta:
       verbose_name_plural = "Nodes"
       verbose_name = "Node"


class nodesAdmin(OSMGeoAdmin):
    list_display = ('Name', 'Latitude', 'Longitude')
    search_fields = ('Name',)
    list_filter = ('Name',)



class Post(models.Model):
    temperature = models.BigIntegerField()
    humidity = models.BigIntegerField()
    published_date = models.DateTimeField(blank=True, null=True)
    node = models.ForeignKey(nodes, null=True, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'Temperature: {self.temperature}, Humidity: {self.humidity}, Published: {self.published_date}'