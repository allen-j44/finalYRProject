import pymongo
from bson import ObjectId  # Import the ObjectId class

# Replace these values with your actual MongoDB connection details
mongo_client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# Access or create a database (replace 'your_database' with your actual database name)
db = mongo_client["ProjectDB"]

# Access or create a collection within the database (replace 'your_collection' with your actual collection name)
collection = db["defsCollection"]

# Your dataset with custom _id field


data = []