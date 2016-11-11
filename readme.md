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
```
* Install mqtt library
```
cd /usr/local/src
git -c http.sslVerify=false clone https://github.com/eclipse/paho.mqtt.python
cd paho.mqtt.python
python setup.py install
```
* download the script and put it in your EV3 home directory (where your 'main' file is). Note: Even though we only need ev3_mqtt_client.py on the EV3s, we clone the whole repository. This helps with debugging and testing as EV3s usually operate without internet access. 
```
cd /home/ev3
git -c http.sslVerify=false clone https://github.com/phil-underscore/S-ENG MQTT
cp MQTT/ev3_mqtt_client.py client.py

```
* Open client script in a editor. Note that we created a copy of `ev3_mqtt_client.py` and called it `client.py`
```
nano client.py
```
and set your robots position (X) in the line `pos = 'X'`
* allow execution
`chmod +x client.py`

## server installation
* setup an wifi AP
* Install paho-mqtt (see above)
* Install mosquitto
`apt-get install mosquitto` 
and run it

* download and run rpi_mqtt_server.py (see client installation above)

## use scripts in c++ code
* Call scripts with ` system("./path_to_script/script.py");` 
* If client.py is in the same directory as your main file (that should be the case if you followed the instructions above) you can just use `system("./client.py");` in c++
* Read return values from `stat` text file.
