
import logging
import time

from blesensor import Sensor

from .service_base import ServiceBase

class TemperatureCollection(ServiceBase):
    def __init__(self):
        super().__init__()

    def job(self):
        logging.info("Running!!")

        mac = "C4:43:D5:0D:4D:F4"

        sensor = Sensor(mac)
        sensor.scan(timeout=20)

        temp = sensor.get("Temperature")
        humidity = sensor.get("Humidity")
        battery = sensor.get("BatteryVoltage")

        logging.info(f"mac: {mac}, temp: {temp}, humidity: {humidity}")

        time.sleep(10)

        return
