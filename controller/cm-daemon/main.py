#!/home/gretel/.pyenv/versions/admin-daemon/bin/python

import logging

import helper

helper.logging.init()


def main():
    logging.info("Start admin-daemon")

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
