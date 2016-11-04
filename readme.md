# MQTT-communications plugin for EV3 robots

These scripts are used to prevent collisions between EV3 robots.
Made for the software engineering lecture at HS Ulm.

It uses [paho-mqtt](https://github.com/eclipse/paho.mqtt.python) as a client and [mosquitto](https://mosquitto.org/) as a broker.


## client installation
* log into your EV3 as root
* Install git:
```
apt-get update
apt-get install git
cd /usr/bin
git -c http.sslVerify=false clone https://github.com/eclipse/paho.mqtt.python
cd paho.mqtt.python
python setup.py install
cd /home/ev3
```
* download the scripts and put them in your EV3 home directory (where your 'main' file is)
* Open client script in a editor
`nano ev3_mqtt_client.py`
and set your robots position in the line
* allow execution
`chmod +x ev3_mqtt_client.py`

## server installation
* setup an wifi AP
* Install mosquitto
`apt-get install mosquitto`

* download and run ev3_mqtt_server.py

## use scripts in c++ code
* Call scripts with ` system("./path_to_script/script.py");`
* Read return values from `stat` text file
