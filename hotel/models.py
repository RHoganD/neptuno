from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


room_type = (
    ('free' , "free"),
    ('reserved' , "reserved"),
)

class Room(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="room_list")
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    room_slug = models.SlugField()
    is_booked = models.BooleanField(default=False)
    capacity = models.IntegerField()
    room_size = models.CharField(max_length=5)
    featured_image = CloudinaryField('image', default='placeholder')
    roomtype = models.CharField(null=True, choices=room_type, max_length=20)

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.category_name


