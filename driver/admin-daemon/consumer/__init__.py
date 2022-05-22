
import time
import logging

from .sensor_state_consumer import SensorStateConsumer


class Consumer(object):
    def __init__(self):
        pass


    def start(self):
        # load service
        sensor_state_consumer = SensorStateConsumer()

        # schedule
        sensor_state_consumer.start()
