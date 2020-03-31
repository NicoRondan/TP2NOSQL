import redis
from functions import getPrice, getTitle

#IP address del host
host = '172.17.0.2'


def connect_db():
        conexion = redis.StrictRedis(host= host, port=6379, db=0, charset="utf-8", decode_responses=True)
        if(conexion.ping()):
            print("conectado al servidor de redis")
        else:
            print("error...")
        return conexion

class Database:
    def __init__(self):
        self.db = connect_db()
    def vacia(self):
        return self.db.dbsize() == 0
    def guardar(self):
        self.db.save()
    def keys(self, formato):
        return self.db.keys(formato)
    def hget(self, key, value):
        return self.db.hget(key, value)
    def hmget(self, key, value):
        return self.db.hmget(key, value)
    def get(self, key):
        return self.db.get(key)
    def existe(self, key):
        return self.db.exists(key) != 0 
    def set(self, key, value):
        self.db.set(key, value)
    def expire(self, key, value):
        self.db.expire(key, value)
    def inicializar(self):
        for x in range(8):
            capitulo = str(x + 1)
            mapping = {
                "titulo": getTitle(capitulo),
                "precio": getPrice(capitulo),
            }
            #Guardamos en la base de datos
            self.db.hmset(capitulo, mapping)
    def reiniciar(self):
        self.db.flushdb()

    



