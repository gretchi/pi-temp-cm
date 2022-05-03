
import logging

from blesensor import Sensor

from .service_base import ServiceBase

class TemperatureCollection(ServiceBase):
    def __init__(self):
        super().__init__()
        self.thread_job()


    def job(self):
        logging.info("Running!!")
