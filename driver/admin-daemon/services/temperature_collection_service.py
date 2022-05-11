
import logging
import time

from service_base import ServiceBase
from temperature_collection import TemperatureCollection

class TemperatureCollectionService(ServiceBase):
    def __init__(self):
        super().__init__()

    def job(self):
        logging.info("Job start")
        worker = TemperatureCollection()
        worker.main()

        return
