
import os
import logging
import time
import random

from blesensor import Sensor

import helper
from mq_client import MqClient


DEVELOP = os.environ.get("DEVELOP")

class TemperatureCollection(object):
    def __init__(self):
        self._dummy_device = {}


    def main(self):
        logging.info("Job start")
        mac = "C4:43:D5:0D:4D:F4"
        self.mq = MqClient()

        self.bt_work(mac)

        self.mq.close()

    def bt_work(self, mac):
        if DEVELOP == "1":
            temp, humidity, battery = self.dummy_device_function(mac)

        else:
            sensor = Sensor(mac)
            sensor.scan(timeout=20)

            temp = sensor.get("Temperature")
            humidity = sensor.get("Humidity")
            battery = sensor.get("BatteryVoltage")

        logging.info(f"mac: {mac}, temp: {temp}, humidity: {humidity}, battery: {battery}")
        self.mq.publish_sensor_state(mac, temp, humidity, battery)

        time.sleep(10)

        return


    def dummy_device_function(self, mac):
            if mac in self._dummy_device:
                dummy_temp = self._dummy_device[mac]["temp"]
                dummy_humidity = self._dummy_device[mac]["humidity"]
            else:
                dummy_temp = 25
                dummy_humidity = 50

            dummy_temp += random.uniform(-0.5, 0.5)
            dummy_humidity += random.uniform(-0.5, 0.5)

            dummy_temp = min(dummy_temp, 30)
            dummy_temp = max(dummy_temp, 20)
            dummy_humidity = min(dummy_humidity, 60)
            dummy_humidity = max(dummy_humidity, 40)

            self._dummy_device[mac] = {
                "temp": dummy_temp,
                "humidity": dummy_humidity,
            }
            temp = int(dummy_temp)
            humidity = int(dummy_humidity)
            battery = 100

            return temp, humidity, battery
