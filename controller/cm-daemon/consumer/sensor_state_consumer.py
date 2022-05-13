
import json
import logging
import sys

from consumer_base import ConsumerBase
import helper

QUEUE_NAME = "sensor_state"

class SensorStateConsumer(ConsumerBase):
    def __init__(self):
        super().__init__()

        self.set_queue(QUEUE_NAME)


    def callback(self, ch, method, properties, body):
        # print(f"Data received: {body}")
        sys.stdout.write(f"\033[32mData received: {body}\033[0m")
        json_body = json.loads(body)

        # mac = json_body.get("mac")
        # temp = json_body.get("temp")
        # humidity = json_body.get("humidity")
        # battery = json_body.get("battery")
        # timestamp = helper.dt.parse(json_body.get("timestamp"))

        # logging.info(mac, temp, humidity, battery, timestamp)
        ch.basic_ack(delivery_tag=method.delivery_tag)

        return
