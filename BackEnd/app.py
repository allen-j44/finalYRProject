#Imports
import datetime
import json
import string
import bcrypt
from flask import Flask, jsonify, request, make_response
import jwt
from pymongo import MongoClient
from bson import ObjectId
from pymongo import aggregation
from functools import wraps
from flask_cors import CORS, cross_origin


#App creation
app = Flask(__name__)
CORS(app)

#Call the monog client, assign the Database and Collection
mongo_client = MongoClient("mongodb://127.0.0.1:27017")
db = mongo_client["playersDB"]
collection = db["playersCollection"]
staff = db.staff