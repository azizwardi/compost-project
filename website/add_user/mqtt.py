
import json
import paho.mqtt.client as mqtt
from django.conf import settings
from .models import *
from .forms import *
import csv 
from datetime import datetime

topics = ['v3/loraatest02@ttn/devices/eui-70b3d57ed005a5c4/up', 'v3/loraatest02@ttn/devices/eui-70b3d57ed005c92e/up', 'v3/loraatest02@ttn/devices/eui-2cf7f1c044900011/up']
def on_connect(mqtt_client, userdata, flags, rc):

    if rc == 0:
        print('Connected successfully')
        
        #hamdi card
        mqtt_client.subscribe(topics[0])

        #yassmin card
        mqtt_client.subscribe(topics[1])
    else:
        print('Bad connection. Code:', rc)

from django.utils import timezone

def on_message(mqtt_client, userdata, msg):
    # Decode the incoming message
    payload_dict = json.loads(msg.payload)
    for topic in topics:
        if msg.topic == topic:
            nodess = nodes.objects.all()
            for node in nodess:
                if msg.topic == f'v3/loraatest02@ttn/devices/{node.ref}/up':
                    temperature = payload_dict['uplink_message']['decoded_payload']['temperature']
                    humidity = payload_dict['uplink_message']['decoded_payload']['humidity']

                    rssi = payload_dict['uplink_message']['rx_metadata'][0]['rssi']
                    snr = payload_dict['uplink_message']['rx_metadata'][0]['snr']

                    print('temperature:', temperature, 'humidity:', humidity, 'rssi:', rssi, 'snr:', snr, '\n')
                    
                    node.RSSI = rssi
                    node.save()
                    node.snr = snr
                    node.save()
                    
                    # Create a new Post object and save it to the database
                    new_data = Post(temperature=temperature, humidity=humidity, node=node)
                    new_data.published_date = timezone.now()
                    new_data.save()


# Create a new MQTT client instance
client = mqtt.Client()

# Set the client's connection and message handling functions
client.on_connect = on_connect
client.on_message = lambda client, userdata, msg: on_message(client, userdata, msg)

# Set the client's username and password
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)

# Connect to the MQTT broker
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)
