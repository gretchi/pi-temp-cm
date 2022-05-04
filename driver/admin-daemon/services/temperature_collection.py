
import logging
import time

from blesensor import Sensor

from .service_base import ServiceBase

class TemperatureCollection(ServiceBase):
    def __init__(self):
        super().__init__()

    def job(self):
        logging.info("Running!!")

        time.sleep(10)

        return
