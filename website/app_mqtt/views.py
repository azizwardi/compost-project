from .models import Post
from django.shortcuts import render

from .mqtt import start_mqtt_client
import json

from django.http import HttpResponse, JsonResponse

#from MQTT_app.mqtt import client as mqtt_client

def start_mqtt(request):
    # Start the MQTT client
    start_mqtt_client()
    
    # Return a simple response to indicate that the client has started
    #return HttpResponse('MQTT client started successfully.')
    return render(request, 'app/test.html', {})



def publish_message(request):
    # Retrieve the latest Post object
    #start_mqtt_client()
    post = Post.objects.order_by('-id').first()

    # Render the template and pass the latest Post object as a context variable
    return render(request, 'app/test.html', {'post': post})