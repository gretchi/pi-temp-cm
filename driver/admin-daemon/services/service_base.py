
import threading
import schedule

class ServiceBase(threading.Thread):
    def __init__(self):
        super(ServiceBase, self).__init__()


    def run(self):
        try:
            self.job()
        except Exception as e:
            logging.error(e)
