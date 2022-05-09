
import json
import redis
import helper

SENSORS_KEY = "sensors"
PLUGS_KEY = "plugs"

class RedisModel(object):
    def __init__(self):
        self.conn = redis.Redis(host='localhost', port=6379, db=0)

    def set_sensor(self, location, mac):
        mac = helper.net.insert_delimiter(mac, "-")


        self.conn.set(SENSORS_KEY, )

    def get_sensors(self):
        pass


    def jget(self, key):
        j = self.conn.get(key)
        data = json.loads(j)

        return data

    def jhset(self, key, data):
        db_data = self.jget(key)
        j = json.dumps(db_data)
        db_data

        self.conn.set(key, j)

        return
