from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Room



class RoomList(generic.ListView):
    model = Room
    # queryset = Room.objects.all()
    queryset = Room.objects.order_by("-category")
    # queryset = Room.objects.all()
    template = 'room_list.html'
    paginate_by = 6





# def room(request):
#     Room = room.object.all()
#     template = 'property/room.html'
#     context = {}
    
#     return render(request, template, context)

# def room_details(request):
#     room_details = Room.object.all()
#     template = 'property/room.html'
#     context = {}
   

