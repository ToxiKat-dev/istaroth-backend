from pymongo import MongoClient
from app import config

connectionString = f"mongodb://{config.MONGO_USERNAME}:{config.MONGO_PASSWORD}@{config.MONGO_IP}:{config.MONGO_PORT}/"
client = MongoClient(connect=connectionString)

DB = client[config.MONGO_DB]
