#!/usr/bin/env python3

import time
import logging

import helper
from consumer import Consumer

helper.logging.init()


def main():
    logging.info("Start cm-daemon")
    consumer = Consumer()

    consumer.start()

    consumer.join()

    logging.info("End cm-daemon")

    return 0



if __name__ == "__main__":
    exit(main())
