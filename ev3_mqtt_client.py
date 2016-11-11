#!/usr/bin/env python

# This scipt will send a status query to the broker and write
# the recieved message to a temporary file ("stat") for use in a c++ program
# '0' : workspace clear
# '1' : neighbour busy
# '2' : connection error
# '9' : network error

# Caution: Very crude script without any safety or security functions
# PROOF OF CONCEPT ONLY!

global pos
pos = '2'

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  if ( rc == 0):
    print("Connection successful!")
    client.subscribe("topic/ev3/status")
    client.publish("topic/ev3/query", "Status?");
  else:
    print("Connection failed with error code " + str(rc))
    write_to_file('2')

def on_message(client, userdata, msg):
  if (msg.topic == "topic/ev3/status"):
    print(msg.payload + " recieved")
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
      write_to_file('0')
    else:
      print("Activity in workspace detected, try again later")
      write_to_file('1')
    client.disconnect()

def start_action():
  client.publish("topic/ev3/query", "busy" + pos)
  print("Workspace free, beginning action")


def end_action():
  client.publish("topic/ev3/query", "free" + pos)
  print("Finished action, workspace is free again")


def write_to_file(msg):
 tmp = open('stat','w')
 tmp.write(msg + "\n")
 tmp.close()

write_to_file('9')

client = mqtt.Client()
client.connect("172.24.1.1",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()


