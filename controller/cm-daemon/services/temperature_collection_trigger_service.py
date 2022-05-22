
import logging
import time

from service_base import ServiceBase
from mq_client import MqClient


class TemperatureCollectionService(ServiceBase):
    def __init__(self):
        super().__init__()

    def job(self):
        logging.info("Job start")
        mac = "C4:43:D5:0D:4D:F4"

        self.mq = MqClient()
        self.mq.publish_sensor_request(mac)

        return
