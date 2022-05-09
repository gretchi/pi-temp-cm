
import logging
import time

from .service_base import ServiceBase

class HelthCheckService(ServiceBase):
    def __init__(self):
        super().__init__()

    def job(self):
        logging.info("Job start")

        # Redisチェック


        return
