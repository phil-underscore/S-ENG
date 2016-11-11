#!/usr/bin/env python

import paho.mqtt.client as mqtt

# This will recieve all status messages and return information 
# on other robots.

# Caution: Very crude script without any safety or security functions
# PROOF OF CONCEPT ONLY!

def on_connect(client, userdata, flags, rc):
  if( rc == 0):
    print("Connection successful!")
    client.subscribe("topic/ev3/query")
  else:
   print("Connection failed with error code "+str(rc))
  
  global stat  
  stat = [0,0,0,0,0,0]  

def on_message(client, userdata, msg):
  global stat
  print("Message recieved")
  if (msg.payload == "Status?"):
    print("Query recieved")
    client.publish("topic/ev3/status", str(stat[1])+str(stat[2])+str(stat[3])+str(stat[4])+str(stat[5]));
    print("Status message sent")
 
  elif "busy" in msg.payload :
    print("Device Nr " + msg.payload[4] + " is now busy")
    stat[int(msg.payload[4])] = 1 
 
  elif "free" in msg.payload :
    print("Device Nr " + msg.payload[4] + " is now free")
    stat[int(msg.payload[4])] = 0
    
client = mqtt.Client()
client.connect("172.24.1.1",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
