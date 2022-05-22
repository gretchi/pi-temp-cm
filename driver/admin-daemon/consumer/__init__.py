
import time
import logging

from .temperature_collection_consumer import TemperatureCollectionConsumer


class Consumer(object):
    def __init__(self):
        pass

    def start(self):
        # load service
        sensor_state_consumer = TemperatureCollectionConsumer()

        # schedule
        sensor_state_consumer.start()
