
import threading
import schedule

class ServiceBase(threading.Thread):
    def __init__(self):
        super(ServiceBase, self).__init__()


    def run(self):
        while True:
            try:
                schedule.run_pending()
            except Exception as e:
                logging.error(e)

            time.sleep(1)
