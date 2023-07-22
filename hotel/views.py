from django.shortcuts import render, get_object_or_404
from django.views import generic , View
from .models import Room ,  Category, Booking
from .forms import ReviewForm

   

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
   
        

def review(self, request, slug, *args, **kwargs):

        queryset = Review.objects.filter(status=1)
        room= get_object_or_404(queryset, slug=slug)
        comments = room.review.filter(approved=True).order_by("-created_on")
        rating = False
        if room.rating.filter(id=self.request.user.id).exists():
            rating = True

        review_form = ReviewFormForm(data=request.POST)
        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.post = post
            review.save()
        else:
            review_form = ReviewFormForm()

        return render(
            request,
            "room_detail.html",
            {
                "review_form": review_form,
                "rating": rating
            },
        )

    # if request.method == 'POST':
    #     checking_date = request.POST.get('checkin')
    #     checkout_date = request.POST.get('checkout')
    #     room = room.objects.get(id = id)
    #     if not check_booking(checkin ,checkout  , id , hotel.room_count):
    #         messages.warning(request, 'Hotel is booked in these dates ')
    #         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    #     HotelBooking.objects.create(hotel=hotel , user = request.user , start_date=checkin
    #     , end_date = checkout , booking_type  = 'reserved')
        
    #     messages.success(request, 'Your booking has been saved')
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

     
    # return render(request , 'room_details.html' ,{
    #     })




def home(generic):
    home =  Room.objects.all()
    template = 'hotel/index.html' 
    context = {
        'index.html' : home
    }
    return render(generic, template, context)


def booking(request):
    queryset = Booking.objects.all()
    template = 'hotel/booking.html'
    context = {
        'booking.html' : booking
    }
    return render(generic, template, context) 


def about(generic):
    about =  Room.objects.all()
    template = 'hotel/about.html' 
    context = {
        'about.html' : about
    }

    return render(generic, template, context)


def contact(generic):
    contact =  Room.objects.all()
    template = 'hotel/contact.html' 
    context = {
        'contact.html' : contact
    }

    return render(generic, template, context)