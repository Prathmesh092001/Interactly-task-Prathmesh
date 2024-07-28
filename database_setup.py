from pymongo import MongoClient

def connect_to_mongo():
    # Connect to MongoDB server running on localhost at the default port 27017
    client = MongoClient('mongodb://localhost:27017/')
    return client

def get_collection(client, db_name, collection_name):
    # Access the specified database and collection
    db = client[db_name]
    collection = db[collection_name]
    return collection

def fetch_documents(collection):
    # Retrieve documents from the collection
    documents = collection.find()
    return documents

def main():
    # Database and collection names
    db_name = 'database'
    collection_name = 'sample_candidate_data'

    try:
        client = connect_to_mongo()
        collection = get_collection(client, db_name, collection_name)
        documents = fetch_documents(collection)

        # Print documents
        for doc in documents:
            print(doc)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
