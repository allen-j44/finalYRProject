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
db = mongo_client["ProjectDB"]
collection = db["playersCollection"]
staff = db.staff

@app.route("/api/v1.0/players", methods=["GET"])
def show_all_players():
    page_num, page_size = 1, 5
    if request.args.get("pn"):
        page_num = int(request.args.get("pn"))
    if request.args.get("ps"):
        page_size = int(request.args.get("ps"))
    page_start = (page_size * (page_num - 1))

    players = collection.find().skip(page_start).limit(page_size)
    players_data = []

    for player in players:
        # Convert ObjectId to string
        player["_id"] = str(player["_id"])
        players_data.append(player)

    return make_response(jsonify(players_data), 200)

# Function to retrieve a single player
@app.route("/api/v1.0/players/<string:id>", methods=["GET"])
def show_one_player(id):
    if len(id) != 24 or not all(c in string.hexdigits for c in id):
        return make_response(jsonify({"error": "Invalid Player ID"}), 404)
    
    player = collection.find_one({"_id": ObjectId(id)})

    if player is not None:
        # Convert ObjectId to string
        player["_id"] = str(player["_id"])
        return make_response(jsonify(player), 200)
    else:
        return make_response(jsonify({"error": "Player not found"}), 404)

if __name__ == '__main__':
    app.run(debug=True)