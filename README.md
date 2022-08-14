## Docker MQTT Sensor

This is a fully customizable MQTT Sensor that runs inside a docker container.
Start the container with the following docker-compose.yml:

    version: '3'

    services:
      sensor1:
        image: mintdaniel42/mqtt-sensor
        build:
          context: ./build
        restart: always
        volumes:
          - <module path>:/module
        devices: []
        environment:
          - MQTT_HOST=<your mqtt broker host>
          - MQTT_PORT=<your mqtt broker port>
          - MQTT_USER=<your mqtt user>
          - MQTT_PASSWORD=<your mqtt password> 
          - MQTT_TOPIC=<your mqtt topic>
          - INTERVAL=60

Then go to "module path" and inside it create a python file named sensor_module.py
that contains at least the following class:

    class SensorHandler:
        def __init__(self):
            pass
    
        def get(self):
            return None

The get() function gets called everytime the container needs new data.