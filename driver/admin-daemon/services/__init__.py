
import schedule

from .temperature_collection import TemperatureCollection


class Services(object):
    def __init__(self):
        self._defined_job()

    def _defined_job(self):
        # load service
        temperature_collection_handle = TemperatureCollection()

        # schedule
        schedule.every(10).seconds.do(temperature_collection_handle.job)
