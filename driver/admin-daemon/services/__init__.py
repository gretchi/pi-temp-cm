
import time
import logging

import schedule

from .service_handler import ServiceHandler
from .temperature_collection import TemperatureCollection

class Services(object):
    def __init__(self):
        self._defined_job()

    def _defined_job(self):
        # load service
        temperature_collection_handle_1 = ServiceHandler(TemperatureCollection)
        temperature_collection_handle_2 = ServiceHandler(TemperatureCollection)

        # schedule
        schedule.every(10).seconds.do(temperature_collection_handle_1.start)
        schedule.every(3).seconds.do(temperature_collection_handle_2.start)


    def run_pending(self):
        schedule.run_pending()
        time.sleep(1)
