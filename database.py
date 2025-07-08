from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://doadmin:i023rwy5A9W84bE6@db-mongodb-nyc3-49937-cf057659.mongo.ondigitalocean.com/admin'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
