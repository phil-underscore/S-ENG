#!/usr/bin/env python

# MQTT-Client for ET4 Software Engineering at HS Ulm WS16
# This scipt will send a status query to the broker and write
# the recieved message to a temporary file ("stat") for use in a c++ program

# Caution: Very crude script without any safety or security functions
# PROOF OF CONCEPT ONLY!

global pos
pos = '1'

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  if ( rc == 0):
    print("Connection successful!")
    client.subscribe("topic/ev3/status")
    client.publish("topic/ev3/query", "Status?");
  else:
    print("Connection failed with error code " + str(rc))

def on_message(client, userdata, msg):
  if (msg.topic == "topic/ev3/status"):
    tmp = open('stat','w')
    print(msg.payload + " recieved")
    tmp.write(msg.payload + "\n")
    if(pos == '1'):
      SOI = '0' + msg.payload[int(pos)-1] + msg.payload[int(pos)]
    elif(pos == '5'):
      SOI = msg.payload[int(pos)-2] + msg.payload[int(pos)-1] + '0'
    else:
      SOI = msg.payload[int(pos)-2] + msg.payload[int(pos)-1] + msg.payload[int(pos)]

    if (SOI[1] == '1'):
      end_action()
    elif(SOI == "000"):
      start_action()
    else:
      print("Activity in workspace detected, try again later")      	
    client.disconnect()
	
def start_action():
  client.publish("topic/ev3/query", "busy" + pos)		
  print("Workspace free, beginning action")
  
def end_action():
  client.publish("topic/ev3/query", "free" + pos)
  print("Finished action, workspace is free again")

client = mqtt.Client()
client.connect("172.24.1.1",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

