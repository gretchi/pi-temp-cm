
import threading
import logging

class ConsumerBase(threading.Thread):
    def __init__(self):
        super(ConsumerBase, self).__init__()


    def run(self):
        try:
            logging.info("Job start")
            self.job()
            logging.info("Job end")
        except Exception as e:
            logging.error(e)
