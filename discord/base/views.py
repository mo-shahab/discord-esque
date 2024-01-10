from django.shortcuts import render
from django.http import HttpResponse

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['chatrooms']
collection_name = db['rooms']

# Fetch data from MongoDB
rooms = list(collection_name.find({}, {'_id': 0}))

# Close the MongoDB connection
client.close()

# Create your views here.
def home(request):
    # rooms = list(collection_name.find())
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for r in rooms:
        if r['id'] == int(pk):
            room = r
    context = {'room': room}
            
    return render(request, 'base/room.html', context)