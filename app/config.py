import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

# PATHS
LOGS = os.getenv('LOGS')
TEMP = os.getenv('TEMP')
DATA = os.getenv('DATA')

#MONGO DETAILS
MONGO_DB = os.getenv('MONGO_DB')
MONGO_IP = os.getenv('MONGO_IP')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')

###############
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
###############