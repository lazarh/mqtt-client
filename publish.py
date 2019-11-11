import sys 
from time import sleep
import paho.mqtt.client as mqtt
import configparser
import htu21d, bh1750, bmp180

"""
parse arguments
"""
args = sys.argv
if len(args) == 2:
    config_file = args[1]
else :
    config_file = ''
 
"""
read file config.properties
"""
config = configparser.ConfigParser()
print(config_file)
if config_file != '' :
    config.read(config_file)
else :
    config.read('config.properties')
"""
take parameters
"""
host = config.get('server', 'ip')
port = int(config.get('server', 'port'))
topic_temp = config.get('htu21d', 'topic_temp')
topic_humid = config.get('htu21d', 'topic_humid')
topic_light = config.get('bh1750', 'topic')
topic_temp2 = config.get('bmp180', 'topic_temp')
topic_pres = config.get('bmp180', 'topic_pres')
topic_alt = config.get('bmp180', 'topic_alt')


def on_connect(mosq, obj, rc):
    print("Connected")

def on_publish(client, userdata, mid):
    print("published")

mqttc = mqtt.Client()
"""
assign event callbacks
"""
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
"""
connect
"""
mqttc.connect(host, port, 60)
while True:
    """
    read sensors
    """
    payload_temp = htu21d.readTemp()
    payload_humid = htu21d.readHumid()
    payload_light = int(bh1750.readLight())
    payload_temp2 = bmp180.readTemp()
    payload_pres = bmp180.readPressure()
    payload_alt = bmp180.readAltitude()
    """
    log
    """
    print(host, port, topic_temp, payload_temp)
    print(host, port, topic_humid, payload_humid)
    print(host, port, topic_light, payload_light)
    print(host, port, topic_temp2, payload_temp2)
    print(host, port, topic_pres, payload_pres)
    print(host, port, topic_alt, payload_alt)
    """
    publish
    """
    mqttc.publish(topic_temp, payload_temp, 0)
    mqttc.publish(topic_humid, payload_humid, 0)
    mqttc.publish(topic_light, payload_light, 0)
    mqttc.publish(topic_temp2, payload_temp2, 0)
    mqttc.publish(topic_pres, payload_pres, 0)
    mqttc.publish(topic_alt, payload_alt, 0)

    sleep(600)

# Continue the network loop
# mqttc.loop_forever()

