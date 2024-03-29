import pymongo
from bson import ObjectId  # Import the ObjectId class

# Replace these values with your actual MongoDB connection details
mongo_client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# Access or create a database (replace 'your_database' with your actual database name)
db = mongo_client["ProjectDB"]

# Access or create a collection within the database (replace 'your_collection' with your actual collection name)
collection = db["defsCollection"]

# Your dataset with custom _id field


data = [
    {
        "_id" : ObjectId(),
        "Team": "1s",
        "Name": "Jordan Mills",
        "Age": 33,
        "POS": "DEF",
        "App": 14,
        "Clean Sheets": 2,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 1214
    },
    {
        "_id" : ObjectId(),
        "Team": "1s",
        "Name": "Kyle Moore",
        "Age": 22,
        "POS": "DEF",
        "App": 13,
        "Clean Sheets": 2,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 682
    },
    {
        "_id" : ObjectId(),
        "Team": "1s",
        "Name": "Nathan Crawford",
        "Age": 29,
        "POS": "DEF",
        "App": 14,
        "Clean Sheets": 2,
        "Yellows": 1,
        "Reds": 0,
        "Mins": 1125
    },
    {
        "_id" : ObjectId(),
        "Team": "2s",
        "Name": "Karl Johnston",
        "Age": 40,
        "POS": "DEF",
        "App": 9,
        "Clean Sheets": 1,
        "Yellows": 1,
        "Reds": 0,
        "Mins": 723
    },
    {
        "_id" : ObjectId(),
        "Team": "1s",
        "Name": "Michael Keable",
        "Age": 31,
        "POS": "DEF",
        "App": 12,
        "Clean Sheets": 2,
        "Yellows": 3,
        "Reds": 0,
        "Mins": 1001
    },
    {
        "_id" : ObjectId(),
        "Team": "",
        "Name": "Craig McCullough",
        "Age": 37,
        "POS": "DEF",
        "App": 4,
        "Clean Sheets": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 360
    },
    {
        "_id" : ObjectId(),
        "Team": "2s",
        "Name": "Danny Smyth",
        "Age": 30,
        "POS": "DEF",
        "App": 1,
        "Clean Sheets": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 24
    },
    {
        "_id" : ObjectId(),
        "Team": "2s",
        "Name": "Michael Massey",
        "Age": 38,
        "POS": "DEF",
        "App": 6,
        "Clean Sheets": 0,
        "Yellows": 2,
        "Reds": 2,
        "Mins": 266
    },
    {
        "_id" : ObjectId(),
        "Team": "1s",
        "Name": "Nathan Shaw",
        "Age": 32,
        "POS": "DEF",
        "App": 8,
        "Clean Sheets": 0,
        "Yellows": 1,
        "Reds": 0,
        "Mins": 518
    }
]



# Insert the data into the collection
collection.insert_many(data)

# Close the MongoDB connection
mongo_client.close()