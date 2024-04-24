#Imports
import base64
import datetime
import json
import string
import bcrypt
from flask import Flask, jsonify, request, make_response
from jwt import encode, decode
from pymongo import MongoClient
from bson import ObjectId
from pymongo import aggregation
from functools import wraps
from flask_cors import CORS, cross_origin


#App creation
app = Flask(__name__)
CORS(app)

#Call the monogo client, assign the Database and Collection
mongo_client = MongoClient("mongodb://127.0.0.1:27017")
db = mongo_client["ProjectDB"]
collection = db["playersCollection"]
staff = db.staffCollection

#Add secret key for jwt token

#Functions relating to back-end authentication Token
app.config['SECRET_KEY'] = 'mysecret'

def jwt_required(func):
    @wraps(func)
    def jwt_required_wrapper(*args, **kwargs):
        token = None
        data = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify( { 'message' : 'Token is missing' }), 401
        try:
            data = decode(token, app.config['SECRET_KEY'], algorithms = 'HS256')
            print("Decoded token data:", data)  # Print decoded token data for debugging
        except:
            return jsonify( { 'message' : 'My token is invalid' }), 401
        return func(*args, **kwargs)
    return jwt_required_wrapper

# Login endpoint
@app.route('/api/v1.0/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response(jsonify({'message': 'Invalid username or password'}), 401)

    user = staff.find_one({'username': auth.username})

    if not user or not bcrypt.checkpw(auth.password.encode('utf-8'), user['password']):
        return make_response(jsonify({'message': 'Invalid username or password'}), 401)

    token = encode({'username': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
    return jsonify({'token': token}), 200

# Show All Players
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

# Retrieve a single player by their ID
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
    

# Get Players in a specific POS
@app.route("/api/v1.0/players/position/<string:position>", methods=["GET"])
def get_players_by_position(position):
    players = collection.find({"POS": position})
    players_data = []
    for player in players:
        # Convert ObjectId to string
        player["_id"] = str(player["_id"])
        players_data.append(player)
    if players_data:
        return make_response(jsonify(players_data), 200)
    else:
        return make_response(jsonify({"error": "Players not found for the given position"}), 404)

#Get Player By Name 
@app.route("/api/v1.0/players/name/<string:name>", methods=["GET"])
def get_player_by_name(name):
    player = collection.find_one({"Name": name})
    if player:
        # Convert ObjectId to string
        player["_id"] = str(player["_id"])
        return make_response(jsonify(player), 200)
    else:
        return make_response(jsonify({"error": "Player not found"}), 404)


# Add a new player
@app.route("/api/v1.0/players", methods=["POST"])
def add_new_player():
    # Check if all required fields are present in the request
    print(request.json)
    required_fields = ["team", "name", "age", "pos", "app",  "goal", "clean", "yellows", "reds", "mins"]
    if all(field in request.json for field in required_fields):
        new_player = {
            "Team": request.json["team"],
            "Name": request.json["name"],
            "Age": int(request.json["age"]),
            "POS": request.json["pos"],
            "App": int(request.json["app"]),
            "Goal Involvements": int(request.json["goal"]),
            "Clean Sheets": int(request.json["clean"]),
            "Yellows": int(request.json["yellows"]),
            "Reds": int(request.json["reds"]),
            "Mins": int(request.json["mins"]),
            # Include other fields as needed
        }

        # Add the new player into the collection
        new_player_id = collection.insert_one(new_player)

        # Get the newly inserted player from the database
        inserted_player = collection.find_one({"_id": new_player_id.inserted_id})

        # Convert ObjectId to string
        inserted_player["_id"] = str(inserted_player["_id"])
        print(inserted_player["_id"])

        # Return response with the new player
        return make_response(jsonify(inserted_player), 201)
    else:
        return make_response(jsonify({"error": "Missing or invalid form data"}), 400)


#Delete Player by ID

@app.route("/api/v1.0/players/<string:id>", methods=["DELETE"])
def delete_player(id):

    #Check ID is valid
    if len(id) != 24 or not all(c in '0123456789abcdefABCDEF' for c in id):
        return make_response(jsonify({"error" : f"Invalid Player ID: {id}"}), 400)
    
    result = collection.delete_one({"_id" : ObjectId(id)})

    if result.deleted_count == 1:
        #Check no of players deleted is 1
        return make_response(jsonify({"message" : f"Player with ID {id} has been deleted"}), 200)
    else:
        return make_response(jsonify({"error" : f"Player with ID {id} was not found"}), 404)

#Edit a Players Full Profile
#Do this using x-www-urlencoded in Postamn For Data
@app.route("/api/v1.0/players/<string:id>", methods=["PUT"])
def edit_player(id):

    # Check if ID is valid
    if len(id) != 24 or not all(c in '0123456789abcdefABCDEF' for c in id):
        return make_response(jsonify({"error": "Invalid Player ID"}), 404)

    print("Received Form Data: ", request.form)
    
    # Check if all required fields are present in the request
    required_fields = ["Team", "Name", "Age", "POS", "App", "Goal Involvements", "Clean Sheets", "Yellows", "Reds", "Mins"]
    if all(field in request.form for field in required_fields):
        # Update player details
        result = collection.update_one(
            {"_id": ObjectId(id)},
            {
                "$set": {
                    "Team": request.form["Team"],
                    "Name": request.form["Name"],
                    "Age": int(request.form["Age"]),
                    "POS": request.form["POS"],
                    "App": int(request.form["App"]),
                    "Goal Involvements": int(request.form["Goal Involvements"]),
                    "Clean Sheets": int(request.form["Clean Sheets"]),
                    "Yellows": int(request.form["Yellows"]),
                    "Reds": int(request.form["Reds"]),
                    "Mins": int(request.form["Mins"]),
                    # Add other fields to update as needed
                }
            }      
        )

        # Check if the update was successful
        if result.matched_count == 1:
            # Provide link to the edited player's details
            edit_player_link = f"http://127.0.0.1:5000/api/v1.0/players/{id}"
            return make_response(jsonify({"url": edit_player_link}), 200)
        else:
            return make_response(jsonify({"error": "Invalid Player ID"}), 404)
    else:
        return make_response(jsonify({"error": "Missing Form Data"}), 400)

if __name__ == '__main__':
    app.run(debug=True)