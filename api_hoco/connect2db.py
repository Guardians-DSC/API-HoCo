import pymongo

API_HOCO_DB_URI = "mongodb://bd-mongo:27017/hoco"

MONGO_CLIENT = pymongo.MongoClient(API_HOCO_DB_URI)

DB = MONGO_CLIENT.hoco

