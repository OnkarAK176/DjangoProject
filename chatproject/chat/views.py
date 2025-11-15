from django.shortcuts import render

# Landing page to enter room name
def index(request):
    return render(request, 'chat/index.html')

# Chat room page
def room(request, room_name):
    # Only room_name is needed; messages handled by WebSocket
    return render(request, 'chat/room.html', {'room_name': room_name})
