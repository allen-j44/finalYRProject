import pymongo
from bson import ObjectId  # Import the ObjectId class

# Replace these values with your actual MongoDB connection details
mongo_client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# Access or create a database (replace 'your_database' with your actual database name)
db = mongo_client["ProjectDB"]

# Access or create a collection within the database (replace 'your_collection' with your actual collection name)
collection = db["gksCollection"]

# Your dataset with custom _id field

data = [
    {
        "_id": ObjectId(),
        "name": "David Murphy",
        "DOB": 41,
        "POS": "GK",
        "App": 1,
        "Clean sheets": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 90
    },
    {
        "_id": ObjectId(),
        "name": "Carter Watt",
        "DOB": 21,
        "POS": "GK",
        "App": 4,
        "Clean sheets": 1,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 360
    },
    {
        "_id": ObjectId(),
        "name": "Jonathan Tate",
        "DOB": 40,
        "POS": "GK",
        "App": 3,
        "Clean sheets": 1,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 270
    },
    {
        "_id": ObjectId(),
        "name": "Ross Adair",
        "DOB": 30,
        "POS": "GK",
        "App": 3,
        "Clean sheets": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 270
    },
    {
        "_id": ObjectId(),
        "name": "Miguel Conceicao",
        "DOB": 40,
        "POS": "GK",
        "App": 4,
        "Clean sheets": 0,
        "Yellows": 1,
        "Reds": 0,
        "Mins": 360
    },
    {
        "_id": ObjectId(),
        "name": "Darren McMullan",
        "DOB": 32,
        "POS": "GK",
        "App": 1,
        "Clean sheets": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 90
    },
    {
        "_id": ObjectId(),
        "name": "Carl O'Neill",
        "DOB": 34,
        "POS": "GK",
        "App": 1,
        "Clean sheets": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 90
    },
    {
        "_id": ObjectId(),
        "name": "Paul Devlin",
        "DOB": 33,
        "POS": "GK",
        "App": 0,
        "Clean sheets": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 0
    },
    {
        "_id": ObjectId(),
        "name": "Jamie Gent",
        "DOB": "",
        "POS": "GK",
        "App": 2,
        "Clean sheets": 0,
        "Yellows": 1,
        "Reds": 1,
        "Mins": 140
    }
]

# Insert the data into the collection
collection.insert_many(data)

# Close the MongoDB connection
mongo_client.close()
