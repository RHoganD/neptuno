from django.shortcuts import render, get_object_or_404
from django.views import generic , View
from .models import Room ,  Category

   

# class RoomList():

def room_list(request):
    # model = Room
    room_list = Room.objects.all()
    template = 'hotel/room_list.html'
    context = {

         'room_list' : room_list
    }
    paginate_by = 6
    
    return render(request, template, context)
    

def room_details(request, id):
    room_details = Room.objects.get(id=id)
    template = 'hotel/room_details.html'
    context = {
        'room_details' : room_details
    }

    return render(request, template, context)


def home(generic):
    home =  Room.objects.all()
    template = 'hotel/index.html' 
    context = {
        'index.html' : home
    }
    return render(generic, template, context)


def about(generic):
    about =  Room.objects.all()
    template = 'hotel/about-us.html' 
    context = {
        'about-us.html' : home
    }

    return render(generic, template, context)


def contact(generic):
    contact =  Room.objects.all()
    template = 'hotel/contact.html' 
    context = {
        'contact.html' : home
    }

    return render(generic, template, context)