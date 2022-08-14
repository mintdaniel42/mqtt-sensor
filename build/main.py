# IMPORT LIBRARIES
import importlib
import os
import sys
import time

import paho.mqtt.client as mqtt

# LOAD ENVIRONMENT VARIABLES
MQTT_HOST = os.getenv('MQTT_HOST')
MQTT_PORT = os.getenv('MQTT_PORT')
MQTT_USER = os.getenv('MQTT_USER')
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD')
MQTT_TOPIC = os.getenv('MQTT_TOPIC')
INTERVAL = os.getenv('INTERVAL')

# LOAD SENSOR MODULE
sys.path.append('/module')
sys.path.append('module')
globals()['sensor_module'] = importlib.import_module('sensor_module')


# CLASS MQTTPublisher()
class MQTTPublisher:
    def __init__(self):
        self.host = MQTT_HOST
        self.port = MQTT_PORT
        self.user = MQTT_USER
        self.password = MQTT_PASSWORD
        self.topic = MQTT_TOPIC

        self.client = mqtt.Client()
        self.client.connect(self.host, self.port)

    def publish(self, msg):
        self.client.publish(self.topic, msg)

    def loop(self):
        self.client.loop()

    def close(self):
        self.client.disconnect()


# CLASS Loop()
class Loop:
    def __init__(self):
        self.sensor_handler = sensor_module.SensorHandler()
        self.mqtt_publisher = MQTTPublisher()

    def loop_forever(self):
        try:
            while True:
                self.mqtt_publisher.publish(self.sensor_handler.get())
                self.mqtt_publisher.loop()
                time.sleep(INTERVAL)
        finally:
            self.mqtt_publisher.close()


# CALL CLASS
if __name__ == '__main__':
    Loop()
