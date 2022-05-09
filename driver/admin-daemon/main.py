#!/usr/bin/env python3

import time
import getpass
import logging

import services
import helper

helper.logging.init()


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
