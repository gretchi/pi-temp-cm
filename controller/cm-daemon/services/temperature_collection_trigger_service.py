
import logging
import time

from service_base import ServiceBase
from mq_client import MqClient
from model import Model


class TemperatureCollectionTriggerService(ServiceBase):
    def __init__(self):
        super().__init__()

    def job(self):
        logging.info("Job start")
        mac = "C4:43:D5:0D:4D:F4"

        self.mq = MqClient()
        self.model = Model()

        for row in self.model.get_nodes():
            sensor_mac = row["sensor_mac"]
            location_name = row["location_name"]

            logging.info(
                f"Fetch row: location_name: {location_name}, sensor_mac: {sensor_mac}")

            self.mq.publish_sensor_request(sensor_mac)
