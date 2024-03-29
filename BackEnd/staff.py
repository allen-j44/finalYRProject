from pymongo import MongoClient
import bcrypt

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.playersDB
staff = db.staffCollection

#Create Dataset for the staff used for authentication later

