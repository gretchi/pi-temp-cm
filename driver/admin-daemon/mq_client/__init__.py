
import os
import json
import datetime

import pika

import helper

# MQ_HOST = os.environ.get("MQ_HOST")
MQ_HOST = "rabbitmq"

class MqClient(object):
    def __init__(self):
        credentials = pika.PlainCredentials("system", "system")
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=MQ_HOST, credentials=credentials)
        )
        self.channel = self.connection.channel()


    def publish_sensor_state(self, mac, temp, humidity, battery):
        data = {
            "mac": mac,
            "temp": temp,
            "humidity": humidity,
            "battery": battery,
            "timestamp": helper.dt.now(),
        }

        self.channel.queue_declare(queue='sensor_state', durable=True)
        self.channel.basic_publish(
            exchange="", routing_key="sensor_state", body=json.dumps(data)
        )



    def close(self):
        self.channel.close()
        self.connection.close()
