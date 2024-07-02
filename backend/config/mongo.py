from os import getenv

from pymongo import MongoClient

MONGO_HOST = getenv('MONGO_HOST', "localhost")
MONGO_PORT = getenv('MONGO_PORT', "27017")

MONGO_DB = getenv('MONGO_DB', 'LatestNews')

client = MongoClient(f'mongodb://{MONGO_HOST}:{MONGO_PORT}')

db = client[MONGO_DB]

