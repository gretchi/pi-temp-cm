
import threading
import logging

from mq_client import MqClient


class ConsumerBase(threading.Thread):
    def __init__(self):
        super(ConsumerBase, self).__init__()
        self._queue_name = None

    def run(self):
        try:
            logging.info("Job start")
            self.job()
            logging.info("Job end")
        except Exception as e:
            logging.error(e)

    def job(self):
        self.mq = MqClient()
        while True:
            try:
                self.mq.consuming("", self.callback)
            except Exception as e:
                logging.error(e)

        mq.close()

    def set_queue(self, queue_name):
        self._queue_name = queue_name
