import pymongo
from bson import ObjectId  # Import the ObjectId class

# Replace these values with your actual MongoDB connection details
mongo_client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# Access or create a database (replace 'your_database' with your actual database name)
db = mongo_client["ProjectDB"]

# Access or create a collection within the database (replace 'your_collection' with your actual collection name)
collection = db["atksCollection"]

# Your dataset with custom _id field


data = [
    {
        "Team": "1s",
        "Name": "Nathan Cousins",
        "Age": 22,
        "POS": "ATK",
        "App": 14,
        "Goal Involvements": 12,
        "Yellows": 4,
        "Reds": 0,
        "Mins": 945
    },
    {
        "Team": "2s",
        "Name": "Craig Edwards",
        "Age": 39,
        "POS": "ATK",
        "App": 13,
        "Goal Involvements": 0,
        "Yellows": 5,
        "Reds": 1,
        "Mins": 894
    },
    {
        "Team": "1s",
        "Name": "Curtis Houston",
        "Age": 20,
        "POS": "ATK",
        "App": 14,
        "Goal Involvements": 13,
        "Yellows": 2,
        "Reds": 0,
        "Mins": 1168
    },
    {
        "Team": "1s",
        "Name": "Adam Munn",
        "Age": 21,
        "POS": "ATK",
        "App": 5,
        "Goal Involvements": 3,
        "Yellows": 2,
        "Reds": 0,
        "Mins": 540
    },
    {
        "Team": "2s",
        "Name": "Michael McKeown",
        "Age": 37,
        "POS": "ATK",
        "App": 0,
        "Goal Involvements": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 0
    },
    {
        "Team": "2s",
        "Name": "Jack Bill",
        "Age": 20,
        "POS": "ATK",
        "App": 1,
        "Goal Involvements": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 90
    },
    {
        "Team": "2s",
        "Name": "Calvin Brotherston",
        "Age": 26,
        "POS": "ATK",
        "App": 2,
        "Goal Involvements": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 108
    },
    {
        "Team": "2s",
        "Name": "James Sproule",
        "Age": 37,
        "POS": "ATK",
        "App": 10,
        "Goal Involvements": 0,
        "Yellows": 3,
        "Reds": 1,
        "Mins": 809
    },
    {
        "Team": "2s",
        "Name": "Stephen Steele",
        "Age": 43,
        "POS": "ATK",
        "App": 2,
        "Goal Involvements": 2,
        "Yellows": 1,
        "Reds": 0,
        "Mins": 180
    },
    {
        "Team": "1s",
        "Name": "Jamie Wallace",
        "Age": 28,
        "POS": "ATK",
        "App": 2,
        "Goal Involvements": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 68
    },
    {
        "Team": "2s",
        "Name": "Daniel Orr",
        "Age": 32,
        "POS": "ATK",
        "App": 2,
        "Goal Involvements": 1,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 180
    }
]

# Insert the data into the collection
collection.insert_many(data)

# Close the MongoDB connection
mongo_client.close()