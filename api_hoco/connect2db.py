import pymongo

API_HOCO_DB_URI = "mongodb+srv://hoco:hocop1@hoco-db.6oqk6tj.mongodb.net/hoco"

MONGO_CLIENT = pymongo.MongoClient(API_HOCO_DB_URI)

DB = MONGO_CLIENT.hoco

