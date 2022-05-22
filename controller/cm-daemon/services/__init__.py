
import time
import logging

import schedule

from service_base import ServiceHandler
from .temperature_collection_trigger_service import TemperatureCollectionTriggerService
from .helth_check_service import HelthCheckService

class Services(object):
    def __init__(self):
        self._defined_job()


    def _defined_job(self):
        # load service
        temperature_collection_trigger_service_handle = ServiceHandler(TemperatureCollectionTriggerService)

        # schedule
        schedule.every(10).seconds.do(temperature_collection_trigger_service_handle.start)


    def run_pending(self):
        schedule.run_pending()
        time.sleep(1)
