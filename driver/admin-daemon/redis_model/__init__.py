
import redis
import helper


class RedisModel(object):
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379, db=0)

    def set_sensor(self, location, mac):
        mac = helper.net.insert_delimiter(mac, "-")

        self.redis.hset(mac, "location", location)
        self.redis.hset(mac, "mac", mac)


    def comvert_from_mac(self, mac):

        pass
