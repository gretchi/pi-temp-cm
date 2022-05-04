
import time
import logging

import schedule

from .service_handler import ServiceHandler
from .temperature_collection_service import TemperatureCollectionService

class Services(object):
    def __init__(self):
        self._defined_job()

    def _defined_job(self):
        # load service
        temperature_collection_handle = ServiceHandler(TemperatureCollectionService)

        # schedule
        schedule.every(10).seconds.do(temperature_collection_handle.start)


    def run_pending(self):
        schedule.run_pending()
        time.sleep(1)
