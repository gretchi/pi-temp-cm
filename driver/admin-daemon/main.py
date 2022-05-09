#!/home/gretel/.pyenv/versions/admin-daemon/bin/python

import time
import getpass
import logging

import services
from redis_model import RedisModel
import helper

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(threadName)s: %(message)s")


def debug_port():
    pass

def main():
    logging.info("Start admin-daemon")
    debug_port()

    services_handle = services.Services()

    while True:
        try:
            services_handle.run_pending()

        except Exception as e:
            logging.error(e)

        time.sleep(1)

    logging.info("End admin-daemon")

    return 0



if __name__ == "__main__":
    if "root" != getpass.getuser():
        logging.fatal("please run as root")
        exit(1)

    exit(main())
