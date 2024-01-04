from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': 'a good chatroom'},
    {'id': 2, 'name': 'a really good chatroom'},
    {'id': 3, 'name': 'those arent good chatrooms, you know this'}
]

# Create your views here.
def home(request):
    return render(request, 'home.html', {'rooms': rooms})

def room(request):
    return render(request, 'room.html')