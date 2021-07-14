import pyudev
import subprocess
import os
import time
import paho.mqtt.client as mqtt
from json import dumps

MQTT_PUBLISH_TOPIC = os.environ.get("MQTT_PUBLISH_TOPIC")
MQTT_SUB_TOPIC = os.environ.get("MQTT_SUBSCRIBE_TOPIC")
MQTT_HOST = os.environ.get("MQTT_BROKER")

print(f"""
MQTT Config:
MQTT_PUBLISH_TOPIC={MQTT_PUBLISH_TOPIC}
MQTT_SUB_TOPIC={MQTT_SUB_TOPIC}
MQTT_HOST={MQTT_HOST}
""")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_SUB_TOPIC)
    client.publish(MQTT_PUBLISH_TOPIC, dumps({'c': 6}))


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(os.environ.get("MQTT_BROKER"), 1883, 60)
    client.loop_start()
    try:
        print('Building context')
        context = pyudev.Context()
        print('Building monitor')
        monitor = pyudev.Monitor.from_netlink(context)
        print('Filtering')
        monitor.filter_by(subsystem='usb')

        serial = os.environ.get('ADB_SERIAL')

        for action, device in monitor:
            if device.get('ID_SERIAL_SHORT') == serial:
                print(device.get('ID_SERIAL_SHORT'), action)
            if action == 'bind' and device.get('ID_SERIAL_SHORT') == serial:
                client.publish(MQTT_PUBLISH_TOPIC, dumps({'c': 0}))
                time.sleep(2)
                command = f"scrcpy -S -s {serial}"
                print(f'Executing: {command}')
                subprocess.call(command, shell=True)
    except KeyboardInterrupt as ki:
        client.loop_stop()
        print('Bye bye')
    except Exception as e:
        print('Ops!')
        print(e)
