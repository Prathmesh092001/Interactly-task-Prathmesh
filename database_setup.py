from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Step 2: Access the database 'db'
db = client['database']

# Step 3: Access the collection 'sample_candidate_data'
collection = db['sample_candidate_data']

# Step 4: Query the collection (Example: Fetch all documents)
candidates = list(collection.find())

# Print the fetched candidate profiles
for candidate in candidates:
    print(candidate)

# Optional: Close the connection
client.close()
