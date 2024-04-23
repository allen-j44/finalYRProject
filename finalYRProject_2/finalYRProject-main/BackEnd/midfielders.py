import pymongo
from bson import ObjectId  # Import the ObjectId class

# Replace these values with your actual MongoDB connection details
mongo_client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# Access or create a database (replace 'your_database' with your actual database name)
db = mongo_client["ProjectDB"]

# Access or create a collection within the database (replace 'your_collection' with your actual collection name)
collection = db["midsCollection"]

# Your dataset with custom _id field


data = [
    {
        "Team": "1s",
        "Name": "Kurtis Mcclure",
        "Age": 27,
        "POS": "MID",
        "App": 14,
        "Goal Involvements": 6,
        "Yellows": 1,
        "Reds": 0,
        "Mins": 843
    },
    {
        "Team": "2s",
        "Name": "Reece Beattie",
        "Age": 21,
        "POS": "MID",
        "App": 6,
        "Goal Involvements": 1,
        "Yellows": 1,
        "Reds": 0,
        "Mins": 452
    },
    {
        "Team": "1s",
        "Name": "Michael Bell",
        "Age": 38,
        "POS": "MID",
        "App": 11,
        "Goal Involvements": 2,
        "Yellows": 2,
        "Reds": 0,
        "Mins": 839
    },
    {
        "Team": "2s",
        "Name": "Graham Crawford",
        "Age": 33,
        "POS": "MID",
        "App": 7,
        "Goal Involvements": 1,
        "Yellows": 1,
        "Reds": 0,
        "Mins": 508
    },
    {
        "Team": "2s",
        "Name": "Dean Davidson",
        "Age": 26,
        "POS": "MID",
        "App": 5,
        "Goal Involvements": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 223
    },
    {
        "Team": "2s",
        "Name": "Daniel Edgeworth",
        "Age": 31,
        "POS": "MID",
        "App": 6,
        "Goal Involvements": 5,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 483
    },
    {
        "Team": "2s",
        "Name": "Francis Feeney",
        "Age": 39,
        "POS": "MID",
        "App": 9,
        "Goal Involvements": 2,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 783
    },
    {
        "Team": "2s",
        "Name": "Jason Ritchie",
        "Age": 36,
        "POS": "MID",
        "App": 13,
        "Goal Involvements": 2,
        "Yellows": 2,
        "Reds": 0,
        "Mins": 1150
    },
    {
        "Team": "2s",
        "Name": "Ben Hawthorne",
        "Age": 20,
        "POS": "MID",
        "App": 10,
        "Goal Involvements": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 587
    },
    {
        "Team": "2s",
        "Name": "Reece Thompson",
        "Age": 26,
        "POS": "MID",
        "App": 6,
        "Goal Involvements": 0,
        "Yellows": 0,
        "Reds": 1,
        "Mins": 402
    },
    {
        "Team": "1s",
        "Name": "Michael McBride",
        "Age": 28,
        "POS": "MID",
        "App": 4,
        "Goal Involvements": 3,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 296
    },
    {
        "Team": "1s",
        "Name": "James Smith",
        "Age": 33,
        "POS": "MID",
        "App": 10,
        "Goal Involvements": 3,
        "Yellows": 3,
        "Reds": 0,
        "Mins": 900
    },
    {
        "Team": "2s",
        "Name": "Ross Young",
        "Age": 27,
        "POS": "MID",
        "App": 6,
        "Goal Involvements": 1,
        "Yellows": 2,
        "Reds": 1,
        "Mins": 279
    },
    {
        "Team": "2s",
        "Name": "Ross Waide",
        "Age": 21,
        "POS": "MID",
        "App": 6,
        "Goal Involvements": 0,
        "Yellows": 1,
        "Reds": 0,
        "Mins": 525
    },
    {
        "Team": "2s",
        "Name": "Reece Dylan Atkinson",
        "Age": 25,
        "POS": "MID",
        "App": 1,
        "Goal Involvements": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 0
    },
    {
        "Team": "2s",
        "Name": "David Brotherston",
        "Age": 36,
        "POS": "MID",
        "App": 1,
        "Goal Involvements": 0,
        "Yellows": 1,
        "Reds": 0,
        "Mins": 90
    },
    {
        "Team": "2s",
        "Name": "Thomas Dorrian",
        "Age": 32,
        "POS": "MID",
        "App": 1,
        "Goal Involvements": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 9
    },
    {
        "Team": "2s",
        "Name": "Dean Proctor",
        "Age": 30,
        "POS": "MID",
        "App": 3,
        "Goal Involvements": 0,
        "Yellows": 1,
        "Reds": 0,
        "Mins": 174
    },
    {
        "Team": "2s",
        "Name": "Matthew Hall",
        "Age": 28,
        "POS": "MID",
        "App": 4,
        "Goal Involvements": 3,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 360
    },
    {
        "Team": "2s",
        "Name": "Matthew Palmer",
        "Age": 27,
        "POS": "MID",
        "App": 1,
        "Goal Involvements": 0,
        "Yellows": 0,
        "Reds": 0,
        "Mins": 10
    }
]


# Insert the data into the collection
collection.insert_many(data)

# Close the MongoDB connection
mongo_client.close()