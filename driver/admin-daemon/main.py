#!/home/gretel/.pyenv/versions/admin-daemon/bin/python

import time
import getpass
import logging

import services

from redis_model import RedisModel

logging.basicConfig(level=logging.DEBUG, format="<%(levelname)s> %(asctime)s %(threadName)s: %(message)s")


def debug_port():
    model = RedisModel()
    model.set_sensor("ぴー", "10:27:F5:22:07:C9")
    model.set_sensor("そら", "AC:84:C6:51:14:91")

def main():
    debug_port()

    services_handle = services.Services()

    while True:
        try:
            services_handle.run_pending()

        except Exception as e:
            logging.error(e)

        time.sleep(1)

    return 0



if __name__ == "__main__":
    if "root" != getpass.getuser():
        logging.fatal("please run as root")
        exit(1)

    exit(main())
