from pymongo import MongoClient

class MongoDBOperations:
    def __init__(self, connection_string, database_name, collection_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def create(self, document):
        """Creates a new document in the collection."""
        try:
            result = self.collection.insert_one(document)
            return result.inserted_id
        except Exception as e:
            print(f"Error creating document: {e}")
            return None
        
if __name__ == "__main__":
    connection_string = "mongodb://mongo_db:27017/"  # Replace with your connection string
    database_name = "resume_builder"
    collection_name = "resumes"

    mongo_ops = MongoDBOperations(connection_string, database_name, collection_name)

    # Create
    user_id = mongo_ops.create({"name": "Alice", "age": 30})
    print(f"Created user with ID: {user_id}")

