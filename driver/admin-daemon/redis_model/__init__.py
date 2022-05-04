
import redis


class RedisModel(object):
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379, db=0)

    def set_sensor(self, location, mac):
        self.redis.hset("sensor", "location", location)
        self.redis.hset("sensor", "mac", mac)
