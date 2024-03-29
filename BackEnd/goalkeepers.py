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
        "_id" : ObjectId(),
        "Team": "1s",
        "Name": "David Murphy",
        "Age": 41,
        "POS": "GK",
        "App": 1,
        "Clean Sheets": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 90
    },
    {
        "_id" : ObjectId(),
        "Team": "1s",
        "Name": "Carter Watt",
        "Age": 21,
        "POS": "GK",
        "App": 4,
        "Clean Sheets": 1,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 360
    },
    {
        "_id" : ObjectId(),
        "Team": "1s",
        "Name": "Jonathan Tate",
        "Age": 40,
        "POS": "GK",
        "App": 3,
        "Clean Sheets": 1,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 270
    },
    {
        "_id" : ObjectId(),
        "Team": "2s",
        "Name": "Ross Adair",
        "Age": 30,
        "POS": "GK",
        "App": 3,
        "Clean Sheets": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 270
    },
    {
        "_id" : ObjectId(),
        "Team": "1s",
        "Name": "Miguel Conceicao",
        "Age": 40,
        "POS": "GK",
        "App": 4,
        "Clean Sheets": 0,
        "Yellows": 1,
        "Reds": 0,
        "Mins": 360
    },
    {
        "_id" : ObjectId(),
        "Team": "2s",
        "Name": "Darren McMullan",
        "Age": 32,
        "POS": "GK",
        "App": 1,
        "Clean Sheets": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 90
    },
    {
        "_id" : ObjectId(),
        "Team": "1s",
        "Name": "Carl O'Neill",
        "Age": 34,
        "POS": "GK",
        "App": 1,
        "Clean Sheets": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 90
    },
    {
        "_id" : ObjectId(),
        "Team": "2s",
        "Name": "Paul Devlin",
        "Age": 33,
        "POS": "GK",
        "App": 0,
        "Clean Sheets": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 0
    },
    {
        "_id" : ObjectId(),
        "Team": "2s",
        "Name": "Jamie Gent",
        "Age": "",
        "POS": "GK",
        "App": 2,
        "Clean Sheets": 0,
        "Yellows": 1,
        "Reds": 1,
        "Mins": 140
    }
]


# Insert the data into the collection
collection.insert_many(data)

# Close the MongoDB connection
mongo_client.close()
