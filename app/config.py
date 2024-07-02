import os
from dotenv import load_dotenv, dotenv_values
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

uri = os.getenv("MONGODB_URL")

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.product_description_generator
db_product_table = db['product_table']  # collection todo_table
