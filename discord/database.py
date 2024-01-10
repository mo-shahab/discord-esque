from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['chatrooms']
collection_name = db['rooms']

rooms_data = [
    {'id': 1, 'name': 'something just like that'},
    {'id': 2, 'name': 'a really good chatroom'},
    {'id': 3, 'name': 'those arent good chatrooms, you know this'}
]

# Inserting data into MongoDB
collection_name.insert_many(rooms_data)

# Close the MongoDB connection
client.close()
