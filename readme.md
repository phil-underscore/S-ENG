# MQTT-communications plugin for EV3 robots

These scripts are used to prevent collisions between EV3 robots.
Made for the software engineering lecture at HS Ulm.

It uses [paho-mqtt](https://github.com/eclipse/paho.mqtt.python) as a client and [mosquitto](https://mosquitto.org/) as a broker.


## client installation
1) log into your EV3 as root
2) Install git:
```
apt-get update
apt-get install git
cd /bin
git clone https://github.com/eclipse/paho.mqtt.python
cd paho.mqtt.python
python setup.py install
cd /home/ev3
```
3) download the scripts and put them in your EV3 home directory (where your 'main' file is)
4) `nano ev3_mqtt_client.py`
and set your robots position in the line
5) `chmod +x ev3_mqtt_client.py`

## server installation
1) setup an wifi AP
2) `apt-get install mosquitto`
3) download and run ev3_mqtt_server.py