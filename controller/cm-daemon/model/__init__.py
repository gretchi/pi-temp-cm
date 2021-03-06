import psycopg2
import psycopg2.extras


class Model(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            host="pgsql",
            port="5432",
            dbname="ptcmdb",
            user="system",
            password="system",
        )

    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def dict_cursor(self):
        self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def get_nodes(self):
        with self.dict_cursor() as cursor:
            query = "SELECT id, sensor_mac, plug_mac, plug_ip, location_name FROM node"
            cursor.execute(query)
            yield cursor.fetchall()

    def add_temperature(self, mac, temp, humidity, battery, sent_at):
        with self.conn.cursor() as cursor:
            query = "INSERT INTO temperature (mac, temp, humidity, battery, sent_at) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (mac, temp, humidity, battery, sent_at))

    def get_temperature_all(self):
        with self.conn.cursor() as cursor:
            query = "SELECT * FROM temperature"
            cursor.execute(query)
            yield cursor.fetchall()

    def add_plug_state(self, mac, status, sent_at):
        with self.conn.cursor() as cursor:
            query = (
                "INSERT INTO temperature (mac, status, sent_at ) VALUES (%s, %s, %s)"
            )
            cursor.execute(query, (mac, status, sent_at))
