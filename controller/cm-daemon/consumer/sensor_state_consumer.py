
import json
import logging

import pika

from .consumer_base import ConsumerBase
from mq_client import MqClient
import helper



class SensorStateConsumer(ConsumerBase):
    def __init__(self):
        super().__init__()

    def job(self):
        mq = MqClient()
        while True:
            try:
                mq.consuming("sensor_state", self.callback)
            except Exception as e:
                logging.error(e)

        mq.close()

    def callback(self, ch, method, properties, body):
        print(f"Data received: {body}")
        json_body = json.loads(body)

        mac = json_body.get("mac")
        temp = json_body.get("temp")
        humidity = json_body.get("humidity")
        battery = json_body.get("battery")
        timestamp = helper.dt.parse(json_body.get("timestamp"))

        logging.info(mac, temp, humidity, battery, timestamp)
